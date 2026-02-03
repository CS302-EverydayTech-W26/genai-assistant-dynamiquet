from gemini_client import *

def main():
    client = GeminiClient()

    while True:
       user_input = input("> ")
       
       if user_input.lower() == "exit":
          print("Goodbye!")
          break
       
       response = client.generate_response(user_input=user_input)
       print(response)

if __name__ == "__main__":
  main()