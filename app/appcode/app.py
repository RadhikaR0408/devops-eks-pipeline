from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import random
import time

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter('app_request_count', 'Total HTTP requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return jsonify({
        "message": "Hello from October's Production-Grade DevOps Demo!",
        "status": "running"
    })

@app.route('/metrics')
def metrics():
    return generate_latest(REQUEST_COUNT), 200, {'Content-Type': CONTENT_TYPE_LATEST}

# Simulate CPU/memory load (optional for dashboard)
@app.route('/simulate_load')
def simulate_load():
    REQUEST_COUNT.inc()
    load = sum([random.random() for _ in range(1000000)])
    return jsonify({"load": load})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
