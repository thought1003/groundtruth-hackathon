# src/generate_captions.py

import os
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")


def generate_captions(
    brand: str,
    product: str,
    n: int = 6,
    out_file: str = "assets/output/captions/captions.txt",
) -> str:
    """
    Uses Gemini to generate n ad-style captions and writes them to a text file.
    Returns the file path.
    """
    out_path = Path(out_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    prompt = f"""
You are a performance marketing copywriter.

Brand: {brand}
Product: {product}

Write {n} short ad captions.

Rules:
- Max 10 words each
- Punchy, modern, scroll-stopping
- No numbering or bullets
- One caption per line
"""

    res = model.generate_content(prompt)
    text = (res.text or "").strip()

    # Clean possible bullets / numbers
    lines = [
        line.strip("•-0123456789. ").strip()
        for line in text.splitlines()
        if line.strip()
    ]
    captions = "\n".join(lines[:n])

    with out_path.open("w", encoding="utf-8") as f:
        f.write(captions)

    return str(out_path)
