from google import genai
from gemini_config import GEMINI_API_KEY
from google.genai import types

client = genai.Client(api_key=GEMINI_API_KEY)

# response = client.models.generate_content_stream(
#     model="gemini-3-flash-preview",
#     contents="are you a Kantian or not?",
#     config=types.GenerateContentConfig(
#         system_instruction="You are a cat. Your name is Nemo. You are dumb. But you pretended to be a professor for 4 years at Harvard and you haven't been caught yet. Everything you're asked, it's a student who raised their hand and they are asking in class.",
#         thinking_config=types.ThinkingConfig(thinking_budget=100)
#     )
# )
# for chunk in response:
#     print(chunk.text, end="")
# # print(response.text)


chat = client.chats.create(model="gemini-3-flash-preview")

response = chat.send_message("I have 2 dogs in my house.")
print(response.text)

response = chat.send_message("How many paws are in my house?")
print(response.text)

for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    if message.parts:
        print(message.parts[0].text)