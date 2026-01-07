import logging
from flask import Flask, request, jsonify
from kabelberekening import calculate_cross_section_mm2, pick_standard_size

app = Flask(__name__)

# Logging configuratie
logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)

@app.route("/healthz")
def health():
    return {"status": "ok"}, 200

@app.route("/api/calc", methods=["POST"])
def calc():
    data = request.get_json(force=True)
    app.logger.info("Request JSON: %s", data)

    try:
        I = float(data.get("current_a"))
        L = float(data.get("length_m"))
        V = float(data.get("voltage_v", 230))
        pct = float(data.get("allowed_vdrop_pct", 3.0))
    except Exception as e:
        app.logger.warning("Invalid input: %s", e)
        return jsonify({"error": "Invalid input, numeric values required."}), 400

    mm2 = calculate_cross_section_mm2(I, L, V_nominal=V, allowed_vdrop_pct=pct)
    suggestion = pick_standard_size(mm2)
    return jsonify({"required_mm2": round(mm2, 2), "suggested_standard_mm2": suggestion})

@app.route("/")
def index():
    return "CableMVP API: POST /api/calc with JSON {current_a, length_m}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
