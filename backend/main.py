from fastapi import FastAPI
from model import predict_risk

app = FastAPI()

@app.get("/")
def home();
    return {"message": "MindTrace AI API running"}

@app.post("/predict")
def risk_prediction(data: dict):

    risk = predict_risk(data)

    return {
        "risk_score": risk,
        "status": "processed"
    }
