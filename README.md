## DAI: Web GenAI-Based Assistant

This project includes a simple Flask web app that lets you chat with a Gemini-powered assistant in your browser.

### Requirements

- Python 3.10+ recommended
- A Google Gemini API key

### Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a local config file with your API key:

```python
# gemini_config.py
GEMINI_API_KEY = "YOUR_API_KEY_HERE"
```

### Run the web app

```bash
python web_assistant.py
```

Then open your browser to:

```
http://127.0.0.1:<port>
```

### Use it

- Type a message into the chat input.
- Press Enter to submit.
- The conversation appears above the input.

### Optional: CLI version

If you want the command-line version instead:

```bash
python cli_assistant.py
```

You can quit the current session by typing ``` exit```
