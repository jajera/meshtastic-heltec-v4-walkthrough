#!/usr/bin/env python3
"""Generate favicon + Open Graph assets matching Patina theme tokens.

Patina slate (social / favicon):
  paper #071014 · cyan #22d3ee · amber #fb923c · muted #b7cdd4 · ink #eef8fa

Patina light (icon fill option):
  cyan #0e7490 · surface #ffffff

Usage:
  .venv/bin/python scripts/generate-brand-assets.py
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets"
OUT.mkdir(parents=True, exist_ok=True)

# Slate tokens (match patina.css [data-md-color-scheme="slate"])
PAPER = (7, 16, 20)  # #071014
SURFACE = (18, 34, 40)  # #122228
CYAN = (34, 211, 238)  # #22d3ee
CYAN_DEEP = (8, 145, 178)  # #0891b2
AMBER = (251, 146, 60)  # #fb923c
INK = (238, 248, 250)  # #eef8fa
MUTED = (183, 205, 212)  # #b7cdd4
BORDER = (47, 85, 96)  # #2f5560

# Light favicon plate (high contrast in browser chrome)
LIGHT_CYAN = (14, 116, 144)  # #0e7490
LIGHT_SURFACE = (255, 255, 255)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = (
        "/usr/share/fonts/liberation-sans-fonts/LiberationSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/liberation-sans-fonts/LiberationSans-Regular.ttf"
    )
    return ImageFont.truetype(path, size)


def lerp(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    t = max(0.0, min(1.0, t))
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))  # type: ignore[return-value]


def draw_lora_mark(
    draw: ImageDraw.ImageDraw,
    cx: int,
    cy: int,
    scale: float,
    color: tuple[int, ...],
    *,
    fill_node: bool = True,
    centered: bool = False,
) -> None:
    """Node + LoRa arcs. Use centered=True for favicon (concentric rings)."""
    stroke = max(2, round(10 * scale))
    node_r = max(3, round(9 * scale))

    if fill_node:
        draw.ellipse(
            (cx - node_r, cy - node_r, cx + node_r, cy + node_r),
            fill=color,
        )
    else:
        draw.ellipse(
            (cx - node_r, cy - node_r, cx + node_r, cy + node_r),
            outline=color,
            width=stroke,
        )

    if centered:
        # Concentric rings around the node — true visual centre
        ring_stroke = max(2, round(5 * scale))
        for r in (14, 24, 34):
            rr = round(r * scale)
            draw.ellipse(
                (cx - rr, cy - rr, cx + rr, cy + rr),
                outline=color,
                width=ring_stroke,
            )
        return

    # Rightward arcs (broadcast) — for OG illustration
    for i, r in enumerate((18, 30, 42)):
        rr = round(r * scale)
        box = (cx - rr // 4, cy - rr, cx + rr, cy + rr)
        start, end = -55, 55
        pad = i * 2
        draw.arc(
            (box[0] - pad, box[1], box[2] + pad, box[3]),
            start,
            end,
            fill=color,
            width=stroke,
        )


def make_icon(size: int) -> Image.Image:
    """Cyan rounded tile + centred white LoRa mark."""
    scale = 8 if size <= 48 else (4 if size <= 180 else 1)
    canvas = size * scale
    img = Image.new("RGB", (canvas, canvas), LIGHT_CYAN)
    draw = ImageDraw.Draw(img)

    pad = max(1, canvas // 18)
    radius = max(4, canvas // 5)
    draw.rounded_rectangle(
        (pad, pad, canvas - pad - 1, canvas - pad - 1),
        radius=radius,
        fill=LIGHT_CYAN,
    )

    # Draw mark on its own layer, then paste centred (avoids stroke asymmetry)
    mark = Image.new("RGBA", (canvas, canvas), (0, 0, 0, 0))
    mark_draw = ImageDraw.Draw(mark)
    mark_scale = canvas / 92
    draw_lora_mark(
        mark_draw,
        canvas // 2,
        canvas // 2,
        mark_scale,
        (*LIGHT_SURFACE, 255),
        centered=True,
    )
    bbox = mark.getbbox()
    if bbox is not None:
        cropped = mark.crop(bbox)
        mx = (canvas - cropped.width) // 2
        my = (canvas - cropped.height) // 2
        img.paste(cropped, (mx, my), cropped)

    if scale > 1:
        img = img.resize((size, size), Image.Resampling.LANCZOS)
    return img


def soft_slate_bg(w: int, h: int) -> Image.Image:
    """Dark paper with cyan glow + faint dot grid (Patina / johna OG style)."""
    img = Image.new("RGB", (w, h), PAPER)
    px = img.load()
    assert px is not None
    for y in range(h):
        for x in range(w):
            dx = (x - w * 0.18) / w
            dy = (y + h * 0.05) / h
            d_c = (dx * dx + dy * dy) ** 0.5
            c = PAPER
            if d_c < 0.9:
                c = lerp(c, (10, 48, 58), (1 - d_c / 0.9) * 0.5)
            dx2 = (x - w * 0.92) / w
            dy2 = (y + h * 0.1) / h
            d_a = (dx2 * dx2 + dy2 * dy2) ** 0.5
            if d_a < 0.65:
                c = lerp(c, (48, 28, 16), (1 - d_a / 0.65) * 0.28)
            c = lerp(c, (4, 10, 12), (y / h) * 0.2)
            if x % 22 == 0 and y % 22 == 0:
                c = lerp(c, CYAN, 0.12)
            px[x, y] = c
    return img


def make_og() -> Image.Image:
    """Clean Patina OG: copy left, large centred mark right — no hardware mock."""
    w, h = 1200, 630
    img = soft_slate_bg(w, h)
    draw = ImageDraw.Draw(img)

    draw.text((72, 130), "HELTEC V4  ·  MESHTASTIC", font=font(24, bold=True), fill=CYAN)
    draw.text((72, 210), "Flash and first setup", font=font(56, bold=True), fill=INK)
    draw.text((72, 300), "Bootloader, web flash, region,", font=font(26), fill=MUTED)
    draw.text((72, 338), "then prove the node is alive.", font=font(26), fill=MUTED)

    chip = (72, 420, 300, 476)
    draw.rounded_rectangle(chip, radius=26, fill=CYAN)
    label = "Start the guide"
    lb = draw.textbbox((0, 0), label, font=font(22, bold=True))
    lw, lh = lb[2] - lb[0], lb[3] - lb[1]
    draw.text(
        ((chip[0] + chip[2] - lw) // 2, (chip[1] + chip[3] - lh) // 2 - 2),
        label,
        font=font(22, bold=True),
        fill=PAPER,
    )

    draw.text(
        (72, 550),
        "meshtastic-heltec-v4-walkthrough.johna.kiwi",
        font=font(20),
        fill=(90, 122, 134),
    )

    draw_lora_mark(draw, 920, 315, 5.5, CYAN, centered=True)

    return img


def save_png(img: Image.Image, name: str) -> None:
    path = OUT / name
    img.save(path, format="PNG", optimize=True)
    print(f"  wrote {path} ({img.size[0]}×{img.size[1]})")


def main() -> None:
    save_png(make_icon(512), "icon-512.png")
    save_png(make_icon(180), "apple-touch-icon.png")
    save_png(make_icon(32), "favicon.png")
    save_png(make_icon(32), "favicon-32.png")
    save_png(make_icon(16), "favicon-16.png")

    ico_path = OUT / "favicon.ico"
    icon32 = make_icon(32)
    icon16 = make_icon(16)
    icon32.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32)], append_images=[icon16])
    print(f"  wrote {ico_path}")

    save_png(make_og(), "og-image.png")
    print(f"\nGenerated brand assets in {OUT}")


if __name__ == "__main__":
    main()
