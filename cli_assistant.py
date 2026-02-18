from gemini_client import *

def main():
    client = GeminiClient()

    print("\n"*10)
    print("Hey, how can I help you?")

    while True:
       user_input = input("> ")
       
       if user_input.lower() == "exit":
          print("Goodbye!")
          break
       
       response = client.generate_response(user_input=user_input)
       print(response)

if __name__ == "__main__":
  main()
  hey()