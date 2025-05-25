from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__, static_folder="static", template_folder="templates")

# OpenRouter API Key
API_KEY = "YOUR-API-KEY"

# Enhance Prompt Function
def enhance_prompt_openrouter(user_prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-4o",
        "messages": [
            {"role": "user", "content": f"Enhance this prompt to make it clearer, detailed, and engaging and please don't add inverted commas: {user_prompt}"}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return None

# Route for the Home Page
@app.route("/")
def home():
    return render_template("index.html")

# API Route for Enhancing Prompt
@app.route("/enhance", methods=["POST"])
def enhance_prompt():
    data = request.get_json()
    user_prompt = data.get("prompt", "")
    enhanced_prompt = enhance_prompt_openrouter(user_prompt)
    return jsonify({"enhanced_prompt": enhanced_prompt})

if __name__ == "__main__":
    app.run(debug=True)
