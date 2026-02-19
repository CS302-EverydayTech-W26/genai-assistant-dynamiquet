from flask import Flask, render_template, request
from gemini_client import GeminiClient

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    chat_input_received = None
    client = GeminiClient()
    
    if request.method == "POST":
        chat_input_received = request.form.get("chat_input")
        
        if chat_input_received and chat_input_received.strip():
            client.generate_response(chat_input_received)

    return render_template('index.html', conversation = client.chat_history)

if __name__ == "__main__":
    app.run()