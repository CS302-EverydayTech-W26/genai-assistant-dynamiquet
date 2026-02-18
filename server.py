from flask import Flask, render_template, request
from gemini_client import GeminiClient

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    chat_input_received = None
    chat_response = None
    
    if request.method == "POST":
        chat_input_received = request.form.get("chat_input")
        client = GeminiClient()
        chat_response = client.generate_response(chat_input_received)

    return render_template('home.html', chat_output = chat_response)

if __name__ == "__main__":
    app.run(port=7000, debug=False)