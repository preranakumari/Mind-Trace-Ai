import numpy as np

def predict_risk(data):

    sleep = data["sleep_hours"]
    activity = data["activity_level"]
    sentiment = data["sentimenet"]

    risk = 0

    if sleep < 5:
        risk += 30

    if activity < 3:
        risk += 30

    if sentiment < 0:
        risk += 40

    return min(risk,100)        