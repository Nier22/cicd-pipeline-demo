from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
    return jsonify({"message": "Welcome to the CI/CD demo API!"})

@app.route("/health")
def health():
    return jsonify({"status": "OK"})

@app.route("/add/<int(a):a>/<int(b):b>")
def add(a: int, b: int):
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)