import os
from dotenv import load_dotenv
from google import genai
from groq import Groq

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

gemini_client = genai.Client(
    api_key=GEMINI_API_KEY
) if GEMINI_API_KEY else None

gemini_client = Groq(
    api_key=GROQ_API_KEY
) if GROQ_API_KEY else None

MODELS = [
    ("Gemini", GEMINI_MODEL),
    ("Groq","openai/gpt-oss-120b"),
    ("Groq","openai/gpt-oss-20b")
]

