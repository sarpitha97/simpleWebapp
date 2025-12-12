from flask import Flask, jsonify, request
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    client_ip = request.remote_addr
    timestamp = datetime.utcnow().isoformat()
    return jsonify({
        "timestamp": timestamp,
        "ip": client_ip
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)