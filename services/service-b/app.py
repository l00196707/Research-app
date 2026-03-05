from flask import Flask, jsonify
import requests

app = Flask(__name__)

SERVICE_C_URL = "http://service-c:5002/data"

@app.route("/health")
def health():
    return "OK",200

@app.route("/process")
def process():
    try:
        response = requests.get(SERVICE_C_URL, timeout=2)
        data = response.json()
        return jsonify({"processed_value" : data["value"] * 2})
    except Exception as e:
        return jsonify({"error": "Service C unavailable"}), 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)