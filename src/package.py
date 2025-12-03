# src/package.py

from pathlib import Path
import zipfile


def package_assets(
    base_dir: str = "assets/output",
    zip_name: str = "creatives_bundle.zip",
) -> str:
    """
    Zips images/ and captions/ under assets/output into a single bundle.
    Returns zip file path.
    """
    base = Path(base_dir)
    zip_path = base / zip_name

    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for sub in ["images", "captions"]:
            folder = base / sub
            if not folder.exists():
                continue
            for f in folder.glob("*.*"):
                arcname = f"{sub}/{f.name}"
                zf.write(f, arcname)

    return str(zip_path)
