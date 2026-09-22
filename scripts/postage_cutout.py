#!/usr/bin/env python3
from __future__ import annotations

import argparse
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps


def stamp_mask(size, bite_ratio=0.048):
    w, h = size
    mask = Image.new("L", (w, h), 255)
    draw = ImageDraw.Draw(mask)
    r = max(6, int(w * bite_ratio))

    top_count = max(7, round(w / (r * 2.15)))
    side_count = max(4, round(h / (r * 2.15)))

    for i in range(1, top_count + 1):
        x = int(i * w / (top_count + 1))
        draw.ellipse((x-r, -r, x+r, r), fill=0)
        draw.ellipse((x-r, h-r, x+r, h+r), fill=0)

    for i in range(1, side_count + 1):
        y = int(i * h / (side_count + 1))
        draw.ellipse((-r, y-r, r, y+r), fill=0)
        draw.ellipse((w-r, y-r, w+r, y+r), fill=0)

    return mask


def crop_centered(img, size, fx, fy):
    w, h = img.size
    cw, ch = size
    cx, cy = int(fx * w), int(fy * h)
    left = max(0, min(w - cw, cx - cw // 2))
    top = max(0, min(h - ch, cy - ch // 2))
    return img.crop((left, top, left + cw, top + ch)), (left, top)


def make_poster(src, output, fx=0.5, fy=0.52):
    W, H = 1080, 1440
    lower_y = 704
    lower_h = H - lower_y

    canvas = Image.new("RGBA", (W, H), (245, 240, 231, 255))
    lower = ImageOps.fit(
        src.convert("RGB"),
        (W, lower_h),
        method=Image.Resampling.LANCZOS
    ).convert("RGBA")

    stamp_w = 340
    stamp_h = round(stamp_w * 2 / 3)
    mask = stamp_mask((stamp_w, stamp_h))

    crop, (left, top) = crop_centered(
        lower, (stamp_w, stamp_h), fx, fy
    )

    hole = Image.new("L", lower.size, 0)
    hole.paste(mask, (left, top))
    lower.putalpha(ImageChops.subtract(lower.getchannel("A"), hole))
    canvas.alpha_composite(lower, (0, lower_y))

    stamp = crop.convert("RGBA")
    stamp.putalpha(mask)

    x = (W - stamp_w) // 2
    y = 230

    shadow_mask = Image.new("L", canvas.size, 0)
    shadow_mask.paste(mask, (x, y + 5))
    shadow_mask = shadow_mask.filter(ImageFilter.GaussianBlur(9))

    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    shadow.putalpha(shadow_mask.point(lambda v: int(v * 0.16)))
    canvas.alpha_composite(shadow)
    canvas.alpha_composite(stamp, (x, y))

    canvas.convert("RGB").save(output, quality=96)


def make_stamp(src, output, width=1200):
    height = round(width * 2 / 3)
    fitted = ImageOps.fit(
        src.convert("RGB"),
        (width, height),
        method=Image.Resampling.LANCZOS
    )
    mask = stamp_mask((width, height))
    result = fitted.convert("RGBA")
    result.putalpha(mask)
    result.save(output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--mode", choices=["poster", "stamp"], default="poster")
    parser.add_argument("--focus-x", type=float, default=0.5)
    parser.add_argument("--focus-y", type=float, default=0.52)
    args = parser.parse_args()

    src = Image.open(args.input).convert("RGB")

    if args.mode == "stamp":
        make_stamp(src, args.output)
    else:
        make_poster(src, args.output, args.focus_x, args.focus_y)


if __name__ == "__main__":
    main()
