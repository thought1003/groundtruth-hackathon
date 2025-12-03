# src/main.py

from pathlib import Path

from .generate_images_local import generate_local_variants
from .generate_captions import generate_captions
from .package import package_assets


def main():
    brand = "Demo Brand"
    product = "Sneaker Campaign"

    print("[main] Starting AI Creative Studio (local Pillow version)...")

    # 1) Image variants
    input_img = "assets/input/product.jpg"
    if not Path(input_img).exists():
        raise FileNotFoundError(f"Base product image not found at {input_img}")

    print("[main] Generating image variants...")
    image_paths = generate_local_variants(input_path=input_img)
    print(f"[main] Generated {len(image_paths)} images.")

    # 2) Captions
    print("[main] Generating captions with Gemini...")
    captions_path = generate_captions(
        brand=brand,
        product=product,
        n=6,
        out_file="assets/output/captions/captions.txt",
    )
    print(f"[main] Captions saved to: {captions_path}")

    # 3) Zip bundle
    print("[main] Packaging creatives...")
    zip_path = package_assets()
    print(f"[main] Bundle ready at: {zip_path}")

    print("[main] DONE – MVP pipeline completed.")


if __name__ == "__main__":
    Path("assets/output/images").mkdir(parents=True, exist_ok=True)
    Path("assets/output/captions").mkdir(parents=True, exist_ok=True)
    main()
