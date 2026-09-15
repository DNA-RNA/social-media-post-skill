# Platform Specifications

## Instagram

| Format | Dimensions | Aspect Ratio | Max Size |
|--------|-----------|--------------|----------|
| Feed Square | 1080×1080px | 1:1 | 30MB |
| Feed Portrait | 1080×1350px | 4:5 | 30MB |
| Feed Landscape | 1080×566px | 1.91:1 | 30MB |
| Stories / Reels | 1080×1920px | 9:16 | 30MB |
| Carousel | 1080×1080px | 1:1 | 30MB |

**Best practices:**
- Portrait (4:5) maximizes feed real estate — preferred for product posts
- Safe zone for Stories text: 250px from top and bottom edges
- JPEG quality ≥ 85% or PNG with transparency

## Facebook

| Format | Dimensions | Aspect Ratio |
|--------|-----------|--------------|
| Feed Post | 1200×630px | 1.91:1 |
| Feed Square | 1200×1200px | 1:1 |
| Stories | 1080×1920px | 9:16 |
| Cover Photo | 820×312px | 2.63:1 |

**Best practices:**
- Text should cover less than 20% of the image area
- Landscape ratio works best for link sharing

## TikTok

| Format | Dimensions | Aspect Ratio |
|--------|-----------|--------------|
| Video | 1080×1920px | 9:16 |
| Cover / Thumbnail | 1080×1920px | 9:16 |
| Profile Photo | 200×200px | 1:1 |

**Best practices:**
- Safe zone for text/UI overlays: 100px from all edges, 300px from bottom
- Vertical format is mandatory for all content

## Platform Selection Logic

When the user hasn't specified a platform:
1. Ask: "Bu post için hangi platform? Instagram, Facebook, TikTok, yoksa hepsi?"
2. If Instagram is confirmed, default to **1080×1350px (4:5 portrait)**
3. If multiple platforms, generate the largest (9:16 = 1080×1920px) and note crop guides for others

## Aspect Ratio Quick Reference

| Ratio | Use Case | Pixel Size |
|-------|----------|-----------|
| 1:1 | Square feed, carousel | 1080×1080 |
| 4:5 | Portrait feed (recommended) | 1080×1350 |
| 9:16 | Stories, Reels, TikTok | 1080×1920 |
| 1.91:1 | Landscape, Facebook | 1080×566 |
