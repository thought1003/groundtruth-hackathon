import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

key = os.getenv("GEMINI_API_KEY")
if not key:
    raise RuntimeError("GEMINI_API_KEY not found")

genai.configure(api_key=key)

models = genai.list_models()

for m in models:
    print(m.name)
