import os
import pickle
import numpy as np
from flask import Flask, request, jsonify,render_template

# Flask app
app = Flask(__name__)

# Base directory (current project folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "model", "scaler.pkl")

# Load model and scaler
model = pickle.load(open(MODEL_PATH, "rb"))
scaler = pickle.load(open(SCALER_PATH, "rb"))

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    recency = float(request.form["Recency"])
    frequency = float(request.form["Frequency"])
    monetary = float(request.form["Monetary"])
    time = float(request.form["Time"])
    # --- simple Risk score logic----
    score=(recency*0.3)+(frequency * 0.3)+(time * 0.4)
    risk_percentage =min(int(score *10),100)
    if risk_percentage<30:
        prediction="Low Risk"
    elif risk_percentage<60:
        prediction="Medium Risk"
    else:
        prediction="High Risk"



    return render_template(
        "result.html",
        prediction=prediction,
        risk_percentage=risk_percentage,
        recency=recency,
        frequency=frequency,
        monetary=monetary,
        time=time

    )

# Main
if __name__ == "__main__":
    app.run(debug=True,port=8000)