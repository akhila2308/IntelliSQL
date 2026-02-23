import os
from dotenv import load_dotenv
from google import genai
from google.genai.types import HttpOptions

load_dotenv()

client = genai.Client(
    api_key=os.getenv("API_KEY"),
    http_options=HttpOptions(api_version="v1")  # 🔥 IMPORTANT FIX
)

def get_response(que, prompt):
    full_prompt = prompt[0] + "\nUser Question:\n" + que

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt,
    )

    return response.text.strip()
