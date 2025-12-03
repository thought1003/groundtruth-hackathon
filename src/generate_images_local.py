# src/generate_images_local.py

from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter, ImageOps


def generate_local_variants(
    input_path: str = "assets/input/product.jpg",
    out_dir: str = "assets/output/images",
    size: int = 1024,
) -> list[str]:
    """
    Takes a base product image and generates 6 simple creative variants locally.
    Returns list of saved image paths.
    """
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    img = Image.open(input_path).convert("RGB")
    img = img.resize((size, size))

    variants = []

    # 1. Base cleaned
    variants.append(img)

    # 2. Warm tone (more color + brightness)
    warm = ImageEnhance.Color(img).enhance(1.5)
    warm = ImageEnhance.Brightness(warm).enhance(1.1)
    variants.append(warm)

    # 3. Cool tone (desaturated + contrast)
    cool = ImageEnhance.Color(img).enhance(0.7)
    cool = ImageEnhance.Contrast(cool).enhance(1.2)
    variants.append(cool)

    # 4. High contrast
    contrast = ImageEnhance.Contrast(img).enhance(1.8)
    variants.append(contrast)

    # 5. Blurred background style
    blur = img.filter(ImageFilter.GaussianBlur(4))
    variants.append(blur)

    # 6. Poster / stylized
    poster = ImageOps.posterize(img, bits=4)
    variants.append(poster)

    saved_paths: list[str] = []
    for i, v in enumerate(variants, start=1):
        fp = out_path / f"creative_{i}.jpg"
        v.save(fp, format="JPEG", quality=90)
        saved_paths.append(str(fp))

    return saved_paths
