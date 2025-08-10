# src/train_model.py
import os, joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load and split data
iris = load_iris(as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.25, random_state=42
)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Save model to outputs folder (Azure ML convention)
os.makedirs("outputs", exist_ok=True)
joblib.dump(model, "outputs/iris_model.pkl")

print("Model trained and saved to outputs/iris_model.pkl")
