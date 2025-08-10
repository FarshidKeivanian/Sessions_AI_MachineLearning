# src/train_param.py
import argparse, os, joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--C", type=float, default=1.0)
    parser.add_argument("--max_iter", type=int, default=200)
    parser.add_argument("--outdir", type=str, default="outputs")
    args = parser.parse_args()

    # Load and split data
    iris = load_iris(as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.25, random_state=42
    )

    # Train model
    model = LogisticRegression(C=args.C, max_iter=args.max_iter)
    model.fit(X_train, y_train)

    # Save model
    os.makedirs(args.outdir, exist_ok=True)
    joblib.dump(model, os.path.join(args.outdir, "iris_model.pkl"))

    print(f"Model trained with C={args.C}, max_iter={args.max_iter}")
    print(f"Saved model to {args.outdir}/iris_model.pkl")