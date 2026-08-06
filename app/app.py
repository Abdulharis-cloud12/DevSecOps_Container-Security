from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps Container Security Pipeline"

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/about")
def about():
    return jsonify({
        "project": "DevSecOps Container Security Pipeline",
        "framework": "Flask",
        "phase": "Phase 2"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
