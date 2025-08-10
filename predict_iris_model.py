# src/predict_model.py
import joblib
import pandas as pd
from sklearn.datasets import load_iris

# Load model
model = joblib.load("outputs/iris_model.pkl")

# Sample data (first 5 rows of iris dataset)
iris = load_iris(as_frame=True)
sample = iris.data.head()

# Predict
preds = model.predict(sample)
print("Sample data:\n", sample)
print("Predicted classes:", preds)
