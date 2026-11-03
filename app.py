from flask import Flask, render_template, jsonify, request
from database.db_manager import init_db, get_dashboard, get_events, add_event, clear_events
from simulation.attack_generator import generate_batch
from simulation.device_simulator import DEVICES
from detection.attack_detector import analyze_event
from datetime import datetime, timezone

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
init_db()

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/dashboard")
def dashboard():
    return jsonify(get_dashboard())

@app.get("/api/events")
def events():
    return jsonify(get_events(limit=100))

@app.post("/api/simulate")
def simulate():
    payload = request.get_json(silent=True) or {}
    count = max(1, min(int(payload.get("count", 8)), 30))
    generated = generate_batch(count)
    for event in generated:
        event = analyze_event(event)
        add_event(event)
    return jsonify({"created": len(generated), "message": f"{len(generated)} synthetic events generated."})

@app.post("/api/clear")
def clear():
    clear_events()
    return jsonify({"message": "Lab event history cleared."})

@app.get("/api/devices")
def devices():
    return jsonify(DEVICES)

if __name__ == "__main__":
    print("IoT Sentinel Fake Lab running at http://127.0.0.1:8000")
    app.run(host="127.0.0.1", port=8000, debug=False)
