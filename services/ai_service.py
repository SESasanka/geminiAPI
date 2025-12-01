from google import genai
import config

client = genai.Client(api_key=config.GEMINI_API_KEY)

def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text
