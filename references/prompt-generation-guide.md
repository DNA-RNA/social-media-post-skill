# Image Generation Prompt Guide

## Prompt Architecture

Every image generation prompt follows this structure:

```
[STYLE_PREFIX] + [PRODUCT_DESCRIPTION] + [MATERIAL_DETAILS] + [SCENE_SETTING] + [LIGHTING] + [COMPOSITION] + [CAMERA_SETTINGS] + [QUALITY_SUFFIX]
```

## Field Definitions

### STYLE_PREFIX
Loaded from `visual-dna.json → generation_prompt.style_prefix`.  
Example: *"Warm Mediterranean luxury aesthetic, editorial product photography,"*

### PRODUCT_DESCRIPTION
Extracted from product image analysis. Include:
- Product type (e.g., "bath towel set", "linen duvet cover")
- Colors with hex-matched descriptors (e.g., "ivory white", "dusty rose")
- Size/form (e.g., "folded neatly", "draped softly", "hanging")

### MATERIAL_DETAILS
Critical for textile products. Describe the fabric:
- Weave type: terry, waffle, satin-stripe, percale, velvet, linen
- Surface quality: plush, crisp, smooth, textured, nubby
- Sheen: matte, slight lustre, high sheen, metallic

Example: *"plush terry cloth with visible loop texture, soft matte finish, heavyweight feel"*

### SCENE_SETTING
From `visual-dna.json → product_presentation.props` and `textures.background_materials`.  
Example: *"placed on warm white marble surface, cotton branch as prop, raw ceramic vessel nearby"*

### LIGHTING
From `visual-dna.json → lighting`.  
Template: *"[type] [temperature] light from [direction], [shadow_intensity] shadows"*  
Example: *"soft diffused natural daylight from the side, warm golden tones, barely-there shadows"*

### COMPOSITION
From `visual-dna.json → composition`.  
Example: *"shallow depth of field, close-up tactile shot, rule of thirds, heavy negative space on the right"*

### CAMERA_SETTINGS
From `visual-dna.json → generation_prompt.camera_settings`.  
Example: *"shot on Hasselblad 500C/M, 120mm macro lens, f/2.8, ISO 100"*

### QUALITY_SUFFIX
Always append:
*"ultra-high resolution, 8K, commercial product photography, no watermark, no text"*

---

## Complete Prompt Examples

### Example 1 — Bath Towel (Instagram 4:5)
```
Warm Mediterranean luxury aesthetic, editorial product photography, 
plush white bath towel with satin stripe border folded in thirds, 
visible terry loop texture, heavyweight cotton weave, 
placed on warm Carrara marble surface with a small raw ceramic soap dish, 
soft diffused natural daylight from the left, warm golden tones, minimal shadows, 
shallow depth of field, close-up tactile composition, heavy negative space above, 
shot on Hasselblad, 120mm lens, f/2, ISO 100, 
ultra-high resolution, 8K, commercial product photography, no watermark, no text
```

### Example 2 — Duvet Cover (Instagram 1:1)
```
Warm Mediterranean luxury editorial, effortless luxury bedroom styling, 
ivory white linen duvet cover with subtle woven texture, naturally rumpled and soft, 
draped over an unseen bed, warm morning sunlight filtering through sheer curtains, 
cotton branch stems leaning against the wall as prop, 
golden hour warmth, soft diffused backlight, dreamy shallow focus, 
overhead-to-eye-level angle, minimalist Scandinavian-Mediterranean composition, 
shot on Sony A7R V, 85mm f/1.4, ISO 200, 
ultra-high resolution, commercial lifestyle photography, no text, no watermark
```

---

## Negative Prompt Template

Always include a negative prompt based on `visual-dna.json → generation_prompt.negative_prompt`:

```
harsh artificial lighting, cool blue tones, cluttered background, 
busy patterns, stock photography feel, plastic textures, 
oversaturated colors, heavy shadows, dark mood, low quality, 
blurry, distorted fabric texture, unrealistic material
```

---

## Fabric-Specific Prompt Additions

| Fabric Type | Prompt Addition |
|-------------|----------------|
| Terry/Toweling | "visible loop pile texture, plush and absorbent appearance, soft matte cotton surface" |
| Satin/Silk | "smooth lustrous surface, subtle sheen, fluid drape, light reflection along folds" |
| Linen | "natural woven texture, slight crinkle, organic imperfection, matte earthy surface" |
| Waffle Weave | "geometric grid texture, spa-like quality, structured yet soft, textured negative space" |
| Velvet | "directional pile, color depth changes with light angle, rich and tactile surface" |
| Percale Cotton | "crisp smooth surface, high thread count appearance, clean and fresh, matte finish" |
| Bamboo | "ultra-smooth silky surface, natural sheen, cool to touch appearance, fine weave" |

---

## Platform Size Mapping

| Platform Format | Kling Ratio | Fal AI `image_size` | DALL-E `size` | Gemini prompt hint |
|----------------|-------------|---------------------|---------------|-------------------|
| Instagram Feed 4:5 | `4:5` | `portrait_4_3` | `1024x1792` | "vertical 4:5 portrait" |
| Instagram Feed 1:1 | `1:1` | `square_hd` | `1024x1024` | "square 1:1 format" |
| Instagram Stories | `9:16` | `portrait_16_9` | `1024x1792` | "vertical 9:16 tall" |
| Facebook Feed | `1.91:1` | `landscape_4_3` | `1792x1024` | "horizontal landscape" |
| TikTok | `9:16` | `portrait_16_9` | `1024x1792` | "vertical 9:16 tall" |

---

## Mannequin & Model Prompt Templates

Use these when a mannequin or human model is present in the source image.

### Template: Headless Tailor's Form (Torso Mannequin)

```
[STYLE_PREFIX]
identical headless tailor's display form, same torso shape and shoulder width, 
same standing position and tilt, no head visible,
now dressed in [PRODUCT_DESCRIPTION] — [FABRIC_TYPE] in [COLOR (#hex)],
[FABRIC_FIT: draping naturally over the form / structured around torso / loosely hanging],
[MATERIAL_DETAILS — texture, pile, sheen],
background: [SCENE_SETTING from visual-dna],
[LIGHTING from visual-dna],
close-up editorial composition, shallow depth of field, tactile fabric detail,
[CAMERA_SETTINGS]
editorial textile photography, ultra-high resolution, 8K, no watermark, no text
```

**Negative:** `different mannequin shape, head added, different body proportions, product floating off form, fabric disconnected from body, re-posed figure, distorted torso`

---

### Template: Full-Body Mannequin

```
[STYLE_PREFIX]
identical full-body retail display mannequin, same rigid upright standing pose, 
same body proportions and silhouette, same arm position,
[mannequin finish: white / beige / chrome — match to source image]
now wearing [PRODUCT_DESCRIPTION] — [FABRIC_TYPE] in [COLOR (#hex)],
[FIT: hanging loosely / fitted to form / draped at hem],
[MATERIAL_DETAILS],
set in: [SCENE_SETTING from visual-dna],
[LIGHTING from visual-dna],
full-body framing, minimalist composition, generous negative space,
[CAMERA_SETTINGS]
commercial fashion product photography, 8K, no watermark, no text
```

**Negative:** `different mannequin, morphed body, re-posed, floating garment, product off body, human skin, face added`

---

### Template: Human Model

```
[STYLE_PREFIX]
same model, same pose, same framing — only the outfit has changed,
model is [approximate build: slender / average / plus-size], [visible body parts: torso / full body / arms],
now wearing [PRODUCT_DESCRIPTION] — [FABRIC_TYPE] in [COLOR (#hex)],
[FIT and DRAPE description], [MATERIAL_DETAILS],
set against: [SCENE_SETTING from visual-dna],
[LIGHTING from visual-dna — same golden warmth, same direction],
[COMPOSITION — same crop, same angle as original],
[CAMERA_SETTINGS]
lifestyle fashion photography, 8K resolution, editorial quality, no watermark, no text
```

**Negative:** `different person, different face, different body type, re-posed, different angle, product floating, fabric not worn`

---

### Mannequin Provider Parameters Quick Reference

| Scenario | Fal AI `strength` | Kling `image_fidelity` | Gemini instruction prefix |
|----------|-------------------|----------------------|--------------------------|
| Headless mannequin | 0.40–0.50 | 0.82 | "KEEP BODY AND POSE IDENTICAL. Only change the garment." |
| Full-body mannequin | 0.42–0.52 | 0.80 | "PRESERVE MANNEQUIN SHAPE AND STANCE EXACTLY. Only re-dress." |
| Human model | 0.45–0.55 | 0.78 | "SAME MODEL SAME POSE. Only the clothing changes." |
| Product only (regular) | 0.65–0.75 | 0.65 | "Use product as reference." |

**Rule:** When in doubt, go lower on strength / higher on fidelity. A slightly less transformed scene is always better than a distorted mannequin.
