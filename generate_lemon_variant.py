import os
import sys
import json
import base64
from datetime import datetime
from pathlib import Path
from PIL import Image as PILImage
import io

OUTPUT_DIR = Path("/Users/ranayalcin/Documents/GitHub/social-media-post-skill/generated-posts")

POSITIVE_PROMPT = """Warm Mediterranean luxury, dolce vita serenity, soft natural diffused daylight, tactile elegance, editorial product photography,
a 2-piece hand towel set beautifully arranged on warm flat Carrara marble surface:
(1) cream-white waffle-weave kitchen towel with dusty rose pink (#C4857A) woven stripe border and charming embroidered donut and cookie motif — folded back and opened to reveal its plush white terry cotton interior, the fold edge showing the dusty rose pink stripe border running along both the outer waffle side and inner terry side, the geometric waffle exterior and embroidered sweet treats motif clearly visible on the outer folded flap,
(2) a dusty rose pink (#C4857A) plush full-size terry cotton hand towel folded neatly beside it — muted rose not hot pink, soft and matte,
matte cotton finish medium weight textile, flat Carrara marble surface,
small dried cotton branch as minimal accent prop in upper-right corner, warm cream beige plaster wall softly blurred behind,
soft diffused natural daylight from the side, warm golden tones, barely-there shadows,
shallow depth of field, close-up editorial composition showing the dual-texture waffle exterior and terry interior with rose stripe border detail, rule of thirds framing, heavy negative space above, vertical 4:5 portrait format for Instagram feed,
shot on Sony A7R V 85mm f/1.8 ISO 200 soft natural side-window light warm amber color grade,
ultra-high resolution 8K commercial product photography no watermark no text overlay"""

NEGATIVE_PROMPT = (
    "harsh lighting, deep black shadows, neon colors, hot pink, bright fuchsia, "
    "cold blue tones, clinical sterile backgrounds, busy cluttered props, "
    "cartoonish or illustrated style, visible text overlays, watermarks, dark dramatic mood, "
    "synthetic plastic-looking materials, HDR effect, "
    "only one towel visible, terry texture hidden, waffle texture not visible"
)

REFERENCE_IMAGES = [
    "/Users/ranayalcin/Downloads/20260827_193804.jpg",
]


def load_image_as_part(path: str):
    from google.genai import types
    with open(path, "rb") as f:
        data = f.read()
    ext = Path(path).suffix.lower()
    mime = "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png"
    return types.Part.from_bytes(data=data, mime_type=mime)


def main():
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        print("HATA: GEMINI_API_KEY env var bulunamadı.")
        sys.exit(1)

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    print("Gemini görsel üretimi başlıyor...")
    print("Model: gemini-3.1-flash-image (Nano Banana 2)")
    print("Referans görseller yükleniyor...")

    contents = []
    for img_path in REFERENCE_IMAGES:
        if Path(img_path).exists():
            contents.append(load_image_as_part(img_path))
            print(f"  + {Path(img_path).name}")

    contents.append(
        "Use this reference image to understand the product: "
        "a 2-piece towel set where the white/cream one has a waffle weave exterior with donut/cookie embroidery and dusty rose pink stripe border, "
        "and its INTERIOR lining is soft white terry cotton (visible when folded open). The stripe border is visible on both sides. "
        "The companion towel is dusty rose pink plush terry cotton. "
        "Now generate a professional Instagram product photo:\n\n" + POSITIVE_PROMPT
    )

    print("\nGörsel üretiliyor (bu 30-60 saniye sürebilir)...")

    response = client.models.generate_content(
        model="models/gemini-3.1-flash-image",
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        ),
    )

    image_data = None
    text_response = ""

    for part in response.candidates[0].content.parts:
        if hasattr(part, "inline_data") and part.inline_data:
            image_data = part.inline_data.data
        elif hasattr(part, "text") and part.text:
            text_response = part.text

    if not image_data:
        print("HATA: Görsel üretilemedi.")
        if text_response:
            print("Model yanıtı:", text_response)
        sys.exit(1)

    output_path = OUTPUT_DIR / f"{timestamp}-havlu-donut-pembe-instagram.png"
    img_bytes = base64.b64decode(image_data) if isinstance(image_data, str) else image_data

    img = PILImage.open(io.BytesIO(img_bytes))
    print(f"\nÜretilen boyut: {img.size[0]}x{img.size[1]}")

    img.save(output_path, "PNG")
    print(f"Kaydedildi: {output_path}")

    metadata = {
        "generated_at": datetime.now().isoformat(),
        "product_type": "havlu-donut-pembe-waffle-terry",
        "platform": "instagram",
        "dimensions": f"{img.size[0]}x{img.size[1]}",
        "target_format": "4:5 portrait (1080x1350)",
        "prompt_used": POSITIVE_PROMPT,
        "negative_prompt": NEGATIVE_PROMPT,
        "provider": "google-gemini",
        "model": "gemini-3.1-flash-image (Nano Banana 2)",
        "mode": "image_to_image_with_references",
        "reference_images": REFERENCE_IMAGES,
        "image_path": str(output_path),
        "visual_dna_version": "Warm Mediterranean Luxury / @dolceev.store",
        "status": "pending_review",
    }

    meta_path = OUTPUT_DIR / f"{timestamp}-havlu-donut-pembe-instagram.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(f"Metadata: {meta_path}")
    print("\nTamamlandı! Görsel: " + str(output_path))
    if text_response:
        print("Model notu:", text_response)


if __name__ == "__main__":
    main()
