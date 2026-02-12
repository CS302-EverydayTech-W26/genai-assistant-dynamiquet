from google import genai
import os
import sys
from google.genai import types
import gemini_config as config
    
class GeminiClient:
    def __init__(self):
        gemini_api_key = config.GEMINI_API_KEY
        if gemini_api_key is None:
            print("Your API key is not set correctly!")
            sys.exit()
        else:
            self.client = genai.Client(api_key=gemini_api_key)
            self.chat_history = []

        self.chat = self.client.chats.create(model='gemini-3-flash-preview')
    def generate_response(self, user_input):
        if self.chat_history is None:  
            return "AI Assistant is not configured correctly"
        
        else:
            system_instruction = "You are a chatbot that always answers with minimal words"
            
            # Add the prompt to the chat history
            self.chat_history += [types.Content(
                  role='user',
                  parts=[types.Part.from_text(text=user_input)]
                )]

            # prompt chatbot
            response = self.chat.send_message(message = user_input,
                                         config=types.GenerateContentConfig(
                                             system_instruction=system_instruction
                                    ))
            response_text = "".join([part.text for part in response.candidates[0].content.parts if part.text])

            # Example: Iterate through parts to avoid the warning
            for part in response.candidates[0].content.parts:
                if part.text:
                    print(part.text)
                elif part.thought:
                    print(f"Thinking: {part.thought}")
                elif part.executable_code:
                    print(f"Code: {part.executable_code.code}")


            # Add response to chat history
            self.chat_history += [types.Content(
                  role='assistant',
                  parts=[types.Part.from_text(text=response_text)] # type: ignore
                )]
            
            return response_text
