# Visual DNA Schema

The Visual DNA is the machine-readable identity of a social media account's aesthetic. It is produced by the `taste-researcher` skill and consumed by `product-visual-analyzer` and `post-compatibility-checker`.

## Schema Definition

```json
{
  "profile": {
    "handle": "@username",
    "platform": "instagram | facebook | tiktok",
    "analyzed_at": "ISO 8601 timestamp",
    "post_sample_count": 12
  },
  "aesthetic": {
    "name": "Human-readable style name, e.g. 'Warm Mediterranean Luxury'",
    "keywords": ["effortless luxury", "tactile", "serene", "editorial"],
    "mood": "calm | bold | playful | minimal | romantic | dramatic",
    "era_reference": "Optional: e.g. '70s editorial', 'modern Scandinavian'"
  },
  "color_palette": {
    "dominant": ["#hex1", "#hex2", "#hex3"],
    "accent": ["#hex4", "#hex5"],
    "forbidden": ["#hex_never_use"],
    "temperature": "warm | cool | neutral",
    "saturation": "muted | balanced | vivid",
    "contrast": "low | medium | high"
  },
  "lighting": {
    "type": "soft_diffused | harsh | rim | backlit | golden_hour | studio",
    "temperature": "warm | cool | neutral",
    "direction": "overhead | side | front | back",
    "shadow_intensity": "none | subtle | strong",
    "notes": "Free-text lighting description"
  },
  "composition": {
    "style": "minimalist | maximalist | editorial | lifestyle | flat_lay | overhead | environmental",
    "depth_of_field": "shallow | deep | mixed",
    "negative_space": "heavy | moderate | minimal",
    "framing": "centered | rule_of_thirds | dynamic | close_up",
    "perspective": "eye_level | overhead | low_angle | diagonal"
  },
  "textures": {
    "present": ["satin", "plush_cotton", "marble", "raw_ceramic", "linen"],
    "tactile_quality": "smooth | rough | layered | mixed",
    "background_materials": ["warm_plaster", "marble", "wood", "fabric"]
  },
  "typography": {
    "style": "serif | sans_serif | script | mixed | none",
    "weight": "light | regular | bold",
    "case": "uppercase | lowercase | mixed",
    "overlay_style": "minimal | decorative | editorial"
  },
  "product_presentation": {
    "context": "in_use | flat_lay | hanging | modeled | environmental | abstract",
    "props": ["cotton_branch", "ceramic_vessel", "marble_surface", "linen_cloth"],
    "human_presence": "none | hands_only | partial | full",
    "branding_visibility": "prominent | subtle | none"
  },
  "platform_adaptations": {
    "instagram": {
      "feed_ratio": "1:1 | 4:5 | 1.91:1",
      "feed_size_px": "1080x1080 | 1080x1350 | 1080x566",
      "stories_size_px": "1080x1920",
      "reels_size_px": "1080x1920"
    },
    "facebook": {
      "post_size_px": "1200x630",
      "stories_size_px": "1080x1920"
    },
    "tiktok": {
      "video_size_px": "1080x1920",
      "cover_size_px": "1080x1920"
    }
  },
  "generation_prompt": {
    "style_prefix": "Ready-to-use prefix for image generation prompts",
    "negative_prompt": "Elements to explicitly avoid",
    "camera_settings": "e.g. 'shot on Hasselblad, 85mm lens, f/1.8'"
  }
}
```

## Usage Rules

- `color_palette.forbidden` must always be respected in generation prompts — never include these colors.
- `generation_prompt.style_prefix` is prepended to every Kling AI prompt.
- `generation_prompt.negative_prompt` is always passed as the negative parameter.
- When `lighting.type` is `golden_hour`, generation prompts must include "warm golden afternoon light, soft shadows".
- When `composition.depth_of_field` is `shallow`, generation prompts must include "shallow depth of field, bokeh background".
