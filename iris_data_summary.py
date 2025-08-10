# src/data_summary.py
import pandas as pd
from sklearn.datasets import load_iris

# Load sample dataset
iris = load_iris(as_frame=True)
df = iris.frame

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nBasic statistics:\n", df.describe())
