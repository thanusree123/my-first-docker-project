from flask import Flask
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Hello from Docker 🚀</h1>
    <p>Time: {datetime.now()}</p>
    <p>Container ID: {socket.gethostname()}</p>
    """

app.run(host="0.0.0.0", port=5000)