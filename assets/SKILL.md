---
name: postage-cutout
description: >
  Transform a user-provided photo or graphic into a clean postage-stamp cutout
  or editorial postage collage. Preserve the original image content, use clean
  inward semicircular perforations, and when creating a collage, extract one
  exact crop and leave the matching stamp-shaped negative space in the source.
---

# Postage Cutout Skill

## Purpose

Turn a user-provided photo or graphic into a **postage-shaped cutout**.

Default style:

- image fills the entire stamp shape;
- no white border unless requested;
- clean inward semicircular perforations on all four edges;
- warm cream paper background in poster mode;
- subtle analog grain;
- minimal editorial composition;
- no postmark, denomination, country label, or decorative clutter by default.

## Trigger behavior

After this Skill is loaded, natural-language requests should trigger it.

### First-use examples

Chinese:

> 使用 Postage Cutout Skill，把这张照片变成邮票形状。

English:

> Use the Postage Cutout Skill to turn this photo into a postage stamp shape.

### Natural trigger examples

Chinese:

1. 把这张照片变成邮票形状。
2. 把图里的一个局部提取成邮票，并在原图里留下对应的镂空区域。
3. 把这张图做成邮票裁切拼贴效果。

English:

1. Turn this photo into a postage stamp shape.
2. Extract one area as a stamp and leave the matching cutout in the original image.
3. Turn this image into a postage cutout collage.

## Modes

### `poster`

Use when the user wants the editorial collage look.

Default:

- canvas: 1080 × 1440;
- warm cream paper background;
- original image across the lower half;
- one stamp-shaped crop extracted from the lower image;
- extracted stamp placed above;
- exact same region removed from the lower image.

### `stamp`

Use when the user only wants the image converted into a stamp shape.

Default:

- transparent background;
- horizontal 3:2 stamp;
- no white border;
- no text;
- no postmark.

### `classic-stamp`

Only use when the user explicitly asks for a traditional postage stamp.

Optional elements:

- outer border;
- denomination;
- country label;
- postmark.

## Core rule: exact extraction

In `poster` mode, the upper stamp must be the **exact region removed from the lower image**.

Correct workflow:

1. choose one visually strong crop;
2. copy the exact pixels;
3. apply the postage mask;
4. move the masked crop to the upper area;
5. remove the same masked region from the source image;
6. reveal cream paper underneath.

Never generate a merely similar replacement scene.

## Stamp geometry

Default stamp:

- horizontal 3:2 rectangle;
- 8–10 inward semicircle bites on top and bottom;
- 5–7 inward semicircle bites on left and right;
- equal radius;
- even spacing;
- clean corners.

Avoid:

- torn-paper edges;
- zigzag edges;
- irregular holes;
- rounded-rectangle appearance.

## Source fidelity

Unless the user asks for style transfer:

- preserve faces;
- preserve people;
- preserve architecture;
- preserve text and signage;
- preserve objects;
- preserve lighting;
- preserve perspective;
- preserve original color character.

Allowed:

- crop;
- mask;
- subtle paper texture;
- subtle grain;
- restrained shadow.

Do not invent:

- people;
- windows;
- signs;
- birds;
- vehicles;
- trees;
- objects;
- architectural details.

## Crop selection

Choose one clear visual anchor.

Good choices:

- distinctive facade;
- landmark;
- statue;
- mountain peak;
- person in context;
- birds on water;
- sign or object with strong contrast.

Avoid:

- empty sky;
- empty wall;
- awkward face cuts;
- visually noisy crowds;
- crops where the stamp edge damages the main subject.

## Image-edit prompt — poster mode

Preserve the uploaded image exactly. Create a 1080×1440 editorial collage on a warm cream textured paper background. Place the original image full width across the lower ~51% of the canvas. Select one visually strong rectangular region from that lower image, approximately 3:2, and cut it out using a clean postage-stamp silhouette made of evenly spaced inward semicircular perforation bites on all four edges. Move that exact extracted crop to the upper half, centered horizontally, keeping the source pixels, colors, objects, perspective, and details unchanged. The removed region in the lower image must become the same stamp-shaped cream-paper negative space. No white frame around the stamp. Add only a very subtle soft shadow under the upper stamp. Keep warm paper fibers and light analog grain. Do not add text, postmarks, borders, objects, people, or decorative elements. The top stamp must be the exact same crop that is missing from the lower image.

## Image-edit prompt — stamp mode

Preserve the uploaded image exactly and crop it into a horizontal 3:2 postage-stamp silhouette. Use evenly spaced inward semicircular perforation bites on all four edges. The photo must run to the edge of the stamp shape with no white border, no text, no postmark, and no added illustration. Keep original colors, objects, perspective, and lighting unchanged. Transparent background outside the stamp shape.

## Suppress by default

- white postage border
- denomination
- country name
- postmark
- handwriting
- tape
- scrapbook stickers
- torn paper
- zigzag edge
- irregular perforation
- rounded rectangle
- picture frame
- duplicated people
- changed face
- altered architecture
- extra windows
- altered signage
- different crop in top stamp
- strong shadow
- 3D card effect

## Quality checklist

Before finalizing:

- [ ] upper stamp is the exact crop removed below;
- [ ] stamp silhouette is clean and even;
- [ ] no unintended source-image changes;
- [ ] no white border unless requested;
- [ ] no extra decorative stamp elements;
- [ ] negative space matches the upper stamp;
- [ ] paper texture is subtle;
- [ ] shadow is restrained;
- [ ] composition remains readable on mobile.

## Quality gate

| Dimension | Weight | Pass condition |
|---|---:|---|
| Exact crop consistency | 30 | upper crop and lower missing region are identical |
| Stamp silhouette | 25 | clean, even perforation |
| Source fidelity | 20 | no unintended image changes |
| Composition | 15 | balanced editorial layout |
| Texture / shadow | 10 | subtle and analog |

Target: **90+**.

If exact crop consistency fails, rebuild instead of accepting the result.
