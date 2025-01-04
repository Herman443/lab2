from flask import Flask, jsonify
import math

app = Flask(__name__)


def numerical_integration(lower, upper, N):
    dx = (upper - lower) / N
    total_area = 0.0
    for i in range(N):
        x = lower + i * dx
        total_area += abs(math.sin(x)) * dx
    return total_area


@app.route("/")
def home():
    return "Flask app for numerical integration is running!"


@app.route("/numericalintegralservice/<lower>/<upper>")
def integration_service(lower, upper):
    low = float(lower)
    upp = float(upper)
    iterations = [10, 100, 1000, 10000, 100000, 1000000]
    results = {}
    for N in iterations:
        results[f"N={N}"] = numerical_integration(low, upp, N)
    return jsonify({"lower": low, "upper": upp, "results": results})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
