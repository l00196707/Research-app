import random, time
from flask import Flask,jsonify

app = Flask(__name__)

FAILURE_RATE = 0

@app.route("/health")
def health():
    """ 
    Health check endpoint
    """
    return "OK", 200

@app.route("/data")
def data():
    """ 
    Data endpoint returning random value
    """
    #simulate latency
    if random.random() < FAILURE_RATE:
        if random.random() < 0.5:
            time.sleep(2) #slow response
        else:
            return jsonify({"error": "simulated failure"}), 500

    value = random.randint(1,100)
    return jsonify({"value": value})


@app.route("/inject_failure/<rate>")
def inject_failure(rate):
    """
    injecting failure rate
    """
    global FAILURE_RATE
    FAILURE_RATE = float(rate)
    return jsonify({"failure_rate": FAILURE_RATE})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
