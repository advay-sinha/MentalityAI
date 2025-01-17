from flask import Flask, request, jsonify
from utils.azure_openai import get_chatbot_response

app = Flask(__name__)

@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    # Get response from Azure OpenAI
    response = get_chatbot_response(user_input)
    return jsonify({"response": response})

@app.route("/")
def home():
    return jsonify({"message": "Azure Chatbot Backend is running!"})

if __name__ == "__main__":
    app.run(debug=True)