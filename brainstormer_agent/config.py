import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

genai.configure(api_key=GOOGLE_API_KEY)

# Model Configurations
FAST_MODEL_NAME = "gemini-1.5-flash-002"
SMART_MODEL_NAME = "gemini-1.5-pro-002"

def get_model(model_name=SMART_MODEL_NAME):
    """Returns a configured GenerativeModel instance."""
    return genai.GenerativeModel(model_name)
