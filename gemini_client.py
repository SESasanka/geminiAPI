from google import genai

client = genai.Client(api_key="AIzaSyCsCoyXa09wAKRuaJ5BL9S9LkX8IRj_CnU")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
