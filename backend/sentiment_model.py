from transformers import pipeline

sentiment = pipeline("sentiment_analysis")

def analyze_text(text):

    result = sentiment(text)[0]

    if result["label"] == "NEGATIVE":
        return -1
    else:
        return 1