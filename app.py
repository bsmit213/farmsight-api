
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "FarmSight API is running."})

@app.route("/api/analyze-image", methods=["POST"])
def analyze_image():
    file = request.files.get("image")
    if not file:
        return jsonify({"error": "No image provided"}), 400
    return jsonify({"diagnosis": "No disease detected", "confidence": "Mocked result"}), 200

@app.route("/api/transcribe-audio", methods=["POST"])
def transcribe_audio():
    file = request.files.get("audio")
    if not file:
        return jsonify({"error": "No audio provided"}), 400
    return jsonify({"transcript": "Sample transcription"}), 200

@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"answer": f"You asked: '{question}'. Here's a mock answer."}), 200

if __name__ == "__main__":
    app.run(debug=True)
