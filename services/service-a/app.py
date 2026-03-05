from flask import Flask, jsonify
import requests

app = Flask(__name__)

SERVICE_B_URL = "http://service-b:5001/process"

@app.route("/health")
def health():
    return "OK",200

@app.route("/compute")
def compute():
    try:
        response = requests.get(SERVICE_B_URL)
        data = response.json()

        return jsonify({
            "final_result": data["processed_value"]
        })
    except Exception as e:
        return jsonify({
            "error": "Service B unavailable",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
