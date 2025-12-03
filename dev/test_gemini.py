import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

key = os.getenv("GEMINI_API_KEY")
print("Gemini key loaded:", key[:10])

if not key:
    raise RuntimeError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-flash-latest")
res = model.generate_content("Write a 5-word ad slogan.")

print("Output:", res.text.strip())
