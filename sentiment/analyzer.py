from transformers import pipeline
import pandas as pd

classifier = pipeline("sentiment-analysis")

def analyze_sentiment(texts):
    results = classifier(texts)
    return pd.DataFrame({
        "Text": texts,
        "Label": [r['label'] for r in results],
        "Score": [r['score'] for r in results]
    })