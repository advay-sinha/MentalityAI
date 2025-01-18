from flask import Flask, request, jsonify
#from flask_cors import CORS
from utils.azure_speech import speech_to_text
from utils.azure_openai import get_chatbot_response


app = Flask(__name__)

@app.route("/utils/azure_speech.py", methods=["POST"])
def speech_to_text_api():
    audio_file = request.files.get("audio")
    if not audio_file:
        return jsonify({"error": "Audio file is required"}), 400

    # Save the file temporarily
    audio_file_path = f"/tmp/{audio_file.filename}"
    audio_file.save(audio_file_path)

    try:
        # Convert speech to text
        transcript = speech_to_text(audio_file_path)
        return jsonify({"transcript": transcript})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route("/api/chatbot-response", methods=["POST"])
def chatbot_response_api():
    data = request.json
    user_input = data.get("user_input")

    if not user_input:
        return jsonify({"error": "User input is required"}), 400

    try:
        # Get response from Azure OpenAI
        response = get_chatbot_response(user_input)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def home():
    return jsonify({"message": "Azure Integrated Backend is running!"})

if __name__ == "__main__":
    #app = Flask(__name__)
    #CORS(app) 
    app.run(debug=True)