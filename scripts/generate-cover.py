#!/usr/bin/env python3
"""Generate deterministic black-and-white cover images for blog posts.

Each blog slug produces a unique, reproducible generative art cover.
Five styles: flow field, mountain ridges, dot matrix, concentric rings, cross hatching.

Usage:
    python scripts/generate-cover.py <slug-or-path>
    python scripts/generate-cover.py we-scanned-every-clawhub-skill
    python scripts/generate-cover.py content/blog/we-scanned-every-clawhub-skill
    python scripts/generate-cover.py --all
    python scripts/generate-cover.py --all --force
    python scripts/generate-cover.py --preview

Requires: pip install Pillow
"""

import argparse
import hashlib
import math
import random
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Pillow is required: pip install Pillow")
    sys.exit(1)

# --- Constants ---

WIDTH = 1200
HEIGHT = 630
SCALE = 2  # Supersample for anti-aliased lines
W = WIDTH * SCALE
H = HEIGHT * SCALE
BG = "white"
FG = "black"
MARGIN = int(40 * SCALE)


# --- Noise ---

class Noise:
    """Perlin-style gradient noise with fractal brownian motion."""

    def __init__(self, seed=0):
        rng = random.Random(seed)
        p = list(range(256))
        rng.shuffle(p)
        self.perm = p + p
        angles = [rng.uniform(0, 2 * math.pi) for _ in range(256)]
        self.grads = [(math.cos(a), math.sin(a)) for a in angles]
        self.grads = self.grads + self.grads

    @staticmethod
    def _fade(t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    @staticmethod
    def _lerp(a, b, t):
        return a + t * (b - a)

    def _grad(self, h, x, y):
        g = self.grads[h & 255]
        return g[0] * x + g[1] * y

    def noise2d(self, x, y):
        xi = int(math.floor(x)) & 255
        yi = int(math.floor(y)) & 255
        xf = x - math.floor(x)
        yf = y - math.floor(y)
        u = self._fade(xf)
        v = self._fade(yf)

        p = self.perm
        aa = p[p[xi] + yi]
        ab = p[p[xi] + yi + 1]
        ba = p[p[xi + 1] + yi]
        bb = p[p[xi + 1] + yi + 1]

        x1 = self._lerp(self._grad(aa, xf, yf), self._grad(ba, xf - 1, yf), u)
        x2 = self._lerp(self._grad(ab, xf, yf - 1), self._grad(bb, xf - 1, yf - 1), u)

        return (self._lerp(x1, x2, v) + 1) / 2

    def fbm(self, x, y, octaves=4, lacunarity=2.0, gain=0.5):
        value = 0.0
        amplitude = 1.0
        frequency = 1.0
        max_val = 0.0
        for _ in range(octaves):
            value += self.noise2d(x * frequency, y * frequency) * amplitude
            max_val += amplitude
            amplitude *= gain
            frequency *= lacunarity
        return value / max_val


# --- Drawing algorithms ---

def draw_flow_field(img, draw, rng, noise):
    """Organic particle traces through a noise field. Pen-plotter aesthetic."""
    num_lines = rng.randint(1200, 2200)
    freq = rng.uniform(0.002, 0.005)
    step = rng.uniform(2, 4) * SCALE
    max_steps = rng.randint(80, 180)
    lw = max(1, SCALE)
    twist = rng.uniform(3.0, 5.0)

    for _ in range(num_lines):
        x = rng.uniform(-W * 0.1, W * 1.1)
        y = rng.uniform(-H * 0.1, H * 1.1)
        pts = []

        for _ in range(max_steps):
            if 0 <= x <= W and 0 <= y <= H:
                pts.append((x, y))
            elif pts:
                break

            angle = noise.fbm(x * freq, y * freq, octaves=3) * math.pi * twist
            x += math.cos(angle) * step
            y += math.sin(angle) * step

        if len(pts) > 3:
            draw.line(pts, fill=FG, width=lw)


def draw_ridges(img, draw, rng, noise):
    """Horizontal lines displaced by noise. Unknown Pleasures aesthetic."""
    num_lines = rng.randint(50, 75)
    line_spacing = (H - 2 * MARGIN) / (num_lines + 1)
    lw = max(2, int(1.5 * SCALE))
    step = 3
    max_peak = H * rng.uniform(0.25, 0.40)  # Tallest peaks = 25-40% of image height
    noise_freq = rng.uniform(0.0015, 0.003)
    seed_offset = rng.uniform(0, 1000)

    # Pre-generate wave parameters per line (2-4 sine components each)
    line_waves = []
    for i in range(num_lines + 1):
        line_rng = random.Random(rng.randint(0, 2**31))
        num_waves = line_rng.randint(2, 4)
        waves = []
        for _ in range(num_waves):
            waves.append({
                'freq': line_rng.uniform(1.5, 5.0),
                'phase': line_rng.uniform(0, 2 * math.pi),
                'amp': line_rng.uniform(0.2, 1.0),
            })
        line_waves.append(waves)

    # Top to bottom: foreground lines occlude background ones
    for i in range(num_lines + 1):
        y_base = MARGIN + line_spacing * (i + 1)
        pts = []
        fill_pts = []

        for px in range(-step, W + step * 2, step):
            t = px / W  # 0..1 across width

            # Bell curve: peaks tallest in center, flat at edges
            cx = (t - 0.5) / 0.3
            center_factor = math.exp(-0.5 * cx * cx)

            # Sum sine waves for main peak shape
            wave = 0
            for w in line_waves[i]:
                wave += math.sin(t * w['freq'] * math.pi + w['phase']) * w['amp']
            wave = max(0, wave)  # Only upward displacement

            # Add noise for organic irregularity
            n = noise.fbm(px * noise_freq + seed_offset, i * 0.35 + seed_offset, octaves=3)
            wobble = (n - 0.5) * max_peak * 0.15

            peak = wave * max_peak * center_factor + wobble * center_factor
            peak = max(0, peak)
            y = y_base - peak
            pts.append((px, y))
            fill_pts.append((px, y))

        # White fill below line to canvas bottom for occlusion
        fill_pts.append((W + step * 2, H + 10))
        fill_pts.append((-step, H + 10))
        draw.polygon(fill_pts, fill=BG)
        draw.line(pts, fill=FG, width=lw)


def draw_dots(img, draw, rng, noise):
    """Grid of circles sized by noise. Halftone aesthetic."""
    spacing = rng.randint(12, 18) * SCALE
    max_r = spacing * 0.48
    freq = rng.uniform(0.002, 0.005)
    octaves = rng.randint(3, 5)
    seed_offset = rng.uniform(0, 1000)

    cols = int((W - 2 * MARGIN) / spacing)
    rows = int((H - 2 * MARGIN) / spacing)
    x_off = (W - cols * spacing) / 2 + spacing / 2
    y_off = (H - rows * spacing) / 2 + spacing / 2

    for row in range(rows):
        for col in range(cols):
            cx = x_off + col * spacing
            cy = y_off + row * spacing
            val = noise.fbm(cx * freq + seed_offset, cy * freq + seed_offset, octaves=octaves)
            # Remap: bottom 20% = no dot, rest scales from tiny to full
            val = max(0, (val - 0.2)) / 0.8
            # Strong power curve for dramatic size contrast
            val = val ** 0.5  # Square root = more large dots, fewer tiny ones
            r = max_r * val
            if r > SCALE * 0.3:
                draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=FG)


def draw_circles(img, draw, rng, noise):
    """Concentric rings with noise displacement. Topographic/wood grain."""
    cx = W * rng.uniform(0.3, 0.7)
    cy = H * rng.uniform(0.3, 0.7)
    num_rings = rng.randint(35, 55)
    max_radius = max(W, H) * 0.9
    ring_spacing = max_radius / num_rings
    lw = max(2, int(1.5 * SCALE))
    segments = 400
    seed_offset = rng.uniform(0, 1000)

    # Multiple distortion fields at different scales for organic look
    freq_lo = rng.uniform(0.08, 0.15)  # Broad bends
    freq_hi = rng.uniform(0.3, 0.6)    # Fine wobble
    disp_lo = rng.uniform(80, 180) * SCALE   # Large displacement
    disp_hi = rng.uniform(15, 40) * SCALE    # Small displacement

    for i in range(num_rings):
        base_r = ring_spacing * (i + 1)
        pts = []
        ring_factor = min(1.0, ((i + 1) / num_rings) ** 0.4)

        for s in range(segments + 1):
            angle = 2 * math.pi * s / segments
            nx = math.cos(angle) * 2.0 + seed_offset
            ny = math.sin(angle) * 2.0 + seed_offset

            # Broad distortion: big smooth bends
            n_lo = noise.fbm(nx * freq_lo + i * 0.06, ny * freq_lo + i * 0.06, octaves=3)
            # Fine distortion: small wobble
            n_hi = noise.fbm(nx * freq_hi + i * 0.12, ny * freq_hi + i * 0.12, octaves=2)

            displacement = (n_lo - 0.5) * disp_lo * ring_factor + (n_hi - 0.5) * disp_hi
            r = base_r + displacement
            px = cx + r * math.cos(angle)
            py = cy + r * math.sin(angle)
            pts.append((px, py))

        if len(pts) > 2:
            draw.line(pts, fill=FG, width=lw)


def draw_hatching(img, draw, rng, noise):
    """Parallel lines at varying angles, density controlled by noise. Engraving aesthetic."""
    num_layers = rng.randint(2, 4)
    base_angle = rng.uniform(0, math.pi)
    freq = rng.uniform(0.002, 0.004)
    lw = max(1, SCALE)
    max_extent = math.sqrt(W ** 2 + H ** 2)

    for layer in range(num_layers):
        angle = base_angle + layer * math.pi / num_layers
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        spacing = rng.randint(4, 7) * SCALE
        num_lines = int(max_extent / spacing)
        # First layer covers most area, each subsequent layer less
        threshold = 0.18 + layer * 0.14

        for i in range(num_lines):
            offset = -max_extent / 2 + i * spacing

            seg_list = []
            current_seg = []
            steps = 180

            for s in range(steps + 1):
                t = s / steps
                px = W / 2 + cos_a * (-max_extent / 2 + t * max_extent) + sin_a * offset
                py = H / 2 + sin_a * (-max_extent / 2 + t * max_extent) - cos_a * offset

                n = noise.fbm(px * freq, py * freq, octaves=4)

                if n > threshold:
                    current_seg.append((px, py))
                else:
                    if len(current_seg) > 1:
                        seg_list.append(current_seg)
                    current_seg = []

            if len(current_seg) > 1:
                seg_list.append(current_seg)

            for seg in seg_list:
                draw.line(seg, fill=FG, width=lw)


# --- Style registry ---

STYLES = {
    "flow": ("Flow Field", draw_flow_field),
    "ridges": ("Mountain Ridges", draw_ridges),
    "dots": ("Dot Matrix", draw_dots),
    "circles": ("Concentric Rings", draw_circles),
    "hatching": ("Cross Hatching", draw_hatching),
}
STYLE_NAMES = list(STYLES.keys())


def style_for_slug(slug):
    h = int(hashlib.sha256(slug.encode()).hexdigest()[:8], 16)
    return STYLE_NAMES[h % len(STYLE_NAMES)]


def seed_for_slug(slug):
    return int(hashlib.sha256(slug.encode()).hexdigest()[:16], 16) & 0x7FFFFFFF


# --- Generation ---

def generate(slug, style_override=None):
    seed = seed_for_slug(slug)
    style_key = style_override or style_for_slug(slug)
    style_name, draw_fn = STYLES[style_key]

    rng = random.Random(seed)
    noise_gen = Noise(seed)

    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw_fn(img, draw, rng, noise_gen)

    # Downsample for anti-aliasing
    img = img.resize((WIDTH, HEIGHT), Image.LANCZOS)
    return img, style_key, style_name


# --- CLI helpers ---

def slug_from_arg(arg):
    arg = arg.rstrip("/")
    parts = arg.split("/")
    slug = parts[-1]
    if slug == "index.md" and len(parts) > 1:
        slug = parts[-2]
    return slug


def find_post_dir(slug):
    for section in ["blog", "use-cases", "comparisons", "industries"]:
        candidate = Path("content") / section / slug
        if candidate.exists() and (candidate / "index.md").exists():
            return candidate
    return None


def generate_for_post(slug_or_path, style=None, force=False):
    slug = slug_from_arg(slug_or_path)
    post_dir = find_post_dir(slug)

    if not post_dir:
        print(f"  skip  {slug} (directory not found)")
        return False

    cover_path = post_dir / "cover.jpg"
    if cover_path.exists() and not force:
        print(f"  skip  {slug} (cover exists)")
        return False

    img, style_key, style_name = generate(slug, style)
    img.save(str(cover_path), "JPEG", quality=95)
    print(f"  done  {slug}  [{style_name}]  -> {cover_path}")
    return True


def generate_all(style=None, force=False):
    count = 0
    generated = 0
    for section in ["blog", "use-cases", "comparisons", "industries"]:
        section_dir = Path("content") / section
        if not section_dir.exists():
            continue
        for post_dir in sorted(section_dir.iterdir()):
            if post_dir.is_dir() and (post_dir / "index.md").exists():
                count += 1
                if generate_for_post(str(post_dir), style, force):
                    generated += 1
    print(f"\n  {generated} generated, {count - generated} skipped, {count} total")


def generate_preview():
    """Grid of all five styles side by side."""
    pad = 20
    cols = len(STYLES)
    grid_w = WIDTH * cols + pad * (cols - 1)
    grid_h = HEIGHT
    grid = Image.new("RGB", (grid_w, grid_h), "#f0f0f0")

    slug = "preview-sample"
    for i, key in enumerate(STYLE_NAMES):
        img, _, style_name = generate(slug, style_override=key)
        grid.paste(img, (i * (WIDTH + pad), 0))
        print(f"  [{i + 1}/{cols}] {style_name}")

    out = Path("cover-styles-preview.jpg")
    grid.save(str(out), "JPEG", quality=95)
    print(f"\n  Saved to {out}  ({grid_w}x{grid_h})")
    print(f"  Styles: {', '.join(STYLE_NAMES)}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate B&W generative art covers for blog posts."
    )
    parser.add_argument(
        "slug", nargs="?",
        help="Blog slug or path (e.g. 'my-post' or 'content/blog/my-post')"
    )
    parser.add_argument("--all", action="store_true", help="Generate for all posts")
    parser.add_argument("--force", action="store_true", help="Overwrite existing covers")
    parser.add_argument("--style", choices=STYLE_NAMES, help="Force a specific style")
    parser.add_argument("--preview", action="store_true", help="Preview grid of all styles")

    args = parser.parse_args()

    if args.preview:
        generate_preview()
    elif args.all:
        generate_all(args.style, args.force)
    elif args.slug:
        generate_for_post(args.slug, args.style, args.force)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
