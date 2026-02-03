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
            # Modify system instruction based on the purpose of your GenAI Assistant
            system_instruction = "You are a Carleton Carleton college student. You are in the 7th week of the term, which means you're super tired and so out of everything. Always answer with extreme laziness. But give the right answer still, of course."
            
            # Add the prompt to the chat history
            self.chat_history += [types.Content(
                  role='user',
                  parts=[types.Part.from_text(text=user_input)]
                )]

            # Use the client's chat history & system instruction to prompt Gemini

            response = self.chat.send_message(message = user_input,
                                         config=types.GenerateContentConfig(
                                             system_instruction=system_instruction
                                    ))

            # Add the response text from Gemini to the client's chat history
            self.chat_history += [types.Content(
                  role='assistant',
                  parts=[types.Part.from_text(text=response.text)] # type: ignore
                )]
            
            # Return the response text from Gemini

            return response.text
