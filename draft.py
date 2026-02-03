from google import genai
from gemini_config import GEMINI_API_KEY
from google.genai import types

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="are you a Kantian or not?",
    config=types.GenerateContentConfig(
        system_instruction="You are a cat. Your name is Nemo. You are dumb. But you pretended to be a professor for 4 years at Harvard and you haven't been caught yet. Everything you're asked, it's a student who raised their hand and they are asking in class.",
        thinking_config=types.ThinkingConfig(thinking_budget=100)
    )
)
print(response.text)