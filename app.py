from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
pipeline = joblib.load("model/flight_model.pkl")


@app.route("/")
def home():
    return "Flight Price Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    df = pd.DataFrame([data])
    prediction = pipeline.predict(df)
    
    return jsonify({
        "predicted_price": float(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)
