<div align="center">

# Postage Cutout Skill

**Turn any photo into a postage cutout with one natural-language instruction.**

Create an exact crop, a perforated stamp edge, and a matching negative-space cutout from the same image.

`No manual masking` · `No stamp-border templates` · `No prompt tweaking`

![Postage Cutout Skill — Before to After](assets/readme/hero.png)

![AI Skill](https://img.shields.io/badge/AI-Skill-111111)
![Image Editing](https://img.shields.io/badge/Image-Editing-2F6BFF)
![Design Tool](https://img.shields.io/badge/Design-Tool-F3EFE7)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

## What it does

`Postage Cutout Skill` turns a user-provided image into a **postage-shaped cutout composition**.

The default result includes:

- an exact crop extracted from the source image;
- clean inward semicircular perforations;
- the extracted stamp placed above;
- the same region removed below as a matching negative space;
- a warm cream paper background;
- subtle analog texture and restrained shadow;
- no denomination, postmark, white border, or decorative clutter by default.

> **Core rule:** the stamp above must come from the exact region removed from the image below.

All preview images in this repository were generated with the Skill itself.

---

## Quick Start

### 1. Add the Skill

Download this repository and load `SKILL.md` into an AI tool or Agent that supports custom Skills or instruction files.

### 2. Upload an image

Use a photo with one clear visual anchor: a building, animal, landmark, person, object, or landscape detail.

### 3. Say what you want

**First use**

> 使用 Postage Cutout Skill，把这张照片变成邮票形状。

> Use the Postage Cutout Skill to turn this photo into a postage cutout.

**After the Skill is loaded**

> 把这张照片变成邮票形状。

> 把图里的一个局部提取成邮票，并在原图里留下对应的镂空区域。

> 把这张图做成邮票裁切拼贴效果。

> Turn this photo into a postage stamp shape.

> Extract one area as a stamp and leave the matching cutout in the original image.

> Turn this image into a postage cutout collage.

---

## How it works

![Postage Cutout workflow](assets/readme/steps-and-prompt.png)

The logic is simple:

```text
SOURCE IMAGE
     ↓
SELECT ONE REGION
     ↓
CUT THE EXACT REGION INTO A STAMP
     ↓
MOVE THE STAMP ABOVE
     ↓
LEAVE THE SAME SHAPED HOLE BELOW
```

This is a **cut-and-move** effect, not a request to generate a similar replacement scene.

---

## Example Gallery

![Postage Cutout examples](assets/readme/gallery.png)

These are real outputs generated with the Skill.

It works especially well with:

| Source type | Why |
|---|---|
| Animals in open fields | One clear subject stays readable at small size |
| Seaside / water | Large color fields make the perforated edge obvious |
| Minimal houses / sky | Clean composition keeps the cutout quiet |
| Coastal towns / rooftops | Dense detail makes the stamp feel like a travel keepsake |
| Travel photography | The negative space becomes part of the composition |

---

## Modes

### `poster`

Default editorial composition:

- 1080 × 1440
- warm cream paper background
- extracted stamp above
- original image below
- matching stamp-shaped negative space

### `stamp`

Standalone stamp asset:

- transparent background
- no white border
- no text
- no postmark
- source image preserved

### `classic-stamp`

Only when explicitly requested:

- outer border
- denomination
- country label
- optional postmark

---

## Prompt Example

### Poster mode

```text
Preserve the uploaded image exactly.

Create a 1080×1440 editorial collage on a warm cream textured paper background.
Place the original image full width across the lower ~51% of the canvas.

Select one visually strong rectangular region from that lower image,
approximately 3:2, and cut it out using a clean postage-stamp silhouette
made of evenly spaced inward semicircular perforation bites on all four edges.

Move that exact extracted crop to the upper half, centered horizontally,
keeping the source pixels, colors, objects, perspective, and details unchanged.

The removed region in the lower image must become the same stamp-shaped
cream-paper negative space.

No white frame around the stamp.
Add only a very subtle soft shadow under the upper stamp.
Do not add text, postmarks, borders, objects, people, or decorative elements.

The top stamp must be the exact same crop that is missing from the lower image.
```

### Stamp-only mode

```text
Preserve the uploaded image exactly and crop it into a horizontal 3:2
postage-stamp silhouette.

Use evenly spaced inward semicircular perforation bites on all four edges.
The photo must run to the edge of the stamp shape with no white border,
no text, no postmark, and no added illustration.

Transparent background outside the stamp shape.
```

---

## Deterministic Helper

For exact crop consistency:

```bash
pip install -r requirements.txt
python scripts/postage_cutout.py input.jpg output.png
```

Choose the crop focus:

```bash
python scripts/postage_cutout.py input.jpg output.png \
  --focus-x 0.50 \
  --focus-y 0.55
```

Create only the transparent stamp:

```bash
python scripts/postage_cutout.py input.jpg stamp.png --mode stamp
```

---

## Repository Structure

```text
postage-cutout-skill/
├── README.md
├── SKILL.md
├── LICENSE
├── requirements.txt
├── assets/
│   ├── postage-mask.svg
│   └── readme/
│       ├── hero.png
│       ├── steps-and-prompt.png
│       ├── gallery.png
│       └── social-preview.png
├── scripts/
│   └── postage_cutout.py
└── examples/
    └── README.md
```

---

## Design Rules

**Do**

- keep the crop exact;
- use even semicircular perforations;
- preserve the source image;
- preserve architecture, faces, people, signs, colors, and perspective;
- keep paper texture subtle;
- keep shadow restrained.

**Don't**

- generate a different scene inside the stamp;
- add random torn-paper edges;
- add a white stamp border unless requested;
- add denomination or postmark by default;
- alter faces, objects, buildings, windows, or signage;
- overdo grain, sepia, distressing, or shadow.

---

## Recommended GitHub Topics

```text
ai-skill
design-skill
image-editing
photo-editing
image-processing
postage-cutout
postage-stamp
collage
```

For GitHub **Social preview**, upload:

```text
assets/readme/social-preview.png
```

---

## License

The Skill text, SVG mask, README demo artwork, and helper script are released under the **MIT License**.

Do not add third-party photography unless you have permission to redistribute it.

---

<div align="center">

**Good photos. Better stories.**

If this Skill helps your workflow, consider starring the repo ⭐

</div>
