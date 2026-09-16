import os
import json
import subprocess
from datetime import datetime
from pathlib import Path
import fal_client

PRODUCT_IMAGE_URL = "https://v3b.fal.media/files/b/0aaa90af/-T-VG2tO74Sgy3Fmd_0jO_3.png"
OUTPUT_DIR = Path("/Users/ranayalcin/Documents/GitHub/social-media-post-skill/generated-posts")

# For Google Nano Banana Pro (edit/img2img):
# Instruction: transform the SCENE only, keep product intact
EDIT_PROMPT = (
    "Keep the towels exactly as they are. Only change the background and lighting. "
    "Place the towels on a warm white marble surface. Add soft natural side-window light "
    "with a warm amber tone and barely-there shadows. Add a small dried cotton branch as "
    "a minimal prop in the background. Make the background a softly blurred warm beige/cream. "
    "Shallow depth of field. Editorial product photography style. "
    "Warm Mediterranean luxury aesthetic. No text, no watermark."
)

NEGATIVE_PROMPT = (
    "harsh lighting, neon colors, cold blue tones, clinical white backgrounds, "
    "busy cluttered props, text overlays, watermarks, dark mood, low quality, blurry"
)


def download(url: str, path: Path):
    subprocess.run(["curl", "-L", "-o", str(path), url], check=True, capture_output=True)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Google Nano Banana Pro (edit) ile üretim başlatılıyor...")
    print(f"Kaynak görsel: {PRODUCT_IMAGE_URL}")

    result = fal_client.subscribe(
        "fal-ai/nano-banana-pro/edit",
        arguments={
            "image_urls": [PRODUCT_IMAGE_URL],
            "prompt": EDIT_PROMPT,
        },
        with_logs=True,
        on_queue_update=lambda u: print(f"  [{getattr(u, 'status', '...')}]"),
    )

    print("\nSonuç anahtarları:", list(result.keys()))

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    # Find image URL in result
    image_url = None
    if "images" in result and result["images"]:
        image_url = result["images"][0].get("url") or result["images"][0].get("image", {}).get("url")
    elif "image" in result:
        image_url = result["image"].get("url") or result["image"]

    if not image_url:
        print("Görsel URL bulunamadı. Ham yanıt:")
        print(json.dumps(result, indent=2)[:1000])
        return

    print(f"Görsel URL: {image_url}")

    output_path = OUTPUT_DIR / f"{timestamp}-havlu-nano-banana-pro.png"
    download(image_url, output_path)
    print(f"Kaydedildi: {output_path}")

    metadata = {
        "generated_at": datetime.now().isoformat(),
        "product_type": "havlu-seti-waffle-nakisli-cupcake",
        "platform": "instagram",
        "dimensions": "portrait (~4:5)",
        "prompt_used": EDIT_PROMPT,
        "negative_prompt": NEGATIVE_PROMPT,
        "provider": "fal-ai",
        "model": "fal-ai/nano-banana-pro/edit",
        "mode": "image_to_image_edit",
        "source_image_url": PRODUCT_IMAGE_URL,
        "image_url": image_url,
        "image_path": str(output_path),
        "visual_dna_version": "Warm Mediterranean Luxury / @dolceev.store",
        "status": "pending_review",
    }

    meta_path = OUTPUT_DIR / f"{timestamp}-havlu-nano-banana-pro.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(f"Metadata: {meta_path}")
    print("\nTamamlandı!")


if __name__ == "__main__":
    main()
