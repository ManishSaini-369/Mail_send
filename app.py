from flask import Flask, jsonify
from threading import Thread
from main import start_monitoring  # 🔗 this connects it

app = Flask(__name__)

@app.route('/')
def home():
    return "Monitoring service is running."

@app.route('/status')
def status():
    return jsonify({"status": "Running", "message": "Email monitoring in background"})

if __name__ == "__main__":
    # 🧵 Start monitor in background thread
    monitor_thread = Thread(target=start_monitoring, daemon=True)
    monitor_thread.start()

    # 🌐 Start Flask server
    app.run(port=5000)
