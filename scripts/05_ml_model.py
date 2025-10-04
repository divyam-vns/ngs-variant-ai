#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

csv_path = Path("reports/variant_summary.csv")
model_out = Path("models/trained_model.pkl")

def make_synthetic(path):
    df = pd.DataFrame({
        "QUAL": [50, 200, 100, 400, 5, 10, 300, 250],
        "DP": [10, 75, 20, 90, 5, 8, 80, 70],
        "label": [0,1,0,1,0,0,1,1]
    })
    df.to_csv(path, index=False)
    return df

def train_model(path, out):
    if not path.exists():
        print("CSV not found — creating small synthetic dataset.")
        df = make_synthetic(path)
    else:
        df = pd.read_csv(path)

    if "label" not in df.columns:
        print("No label column found. Add 'label' column for training.")
        return

    X = df[["QUAL","DP"]].fillna(0)
    y = df["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    joblib.dump(clf, out)
    print(f"Trained model saved to {out} with test accuracy {score:.2f}")

if __name__ == "__main__":
    train_model(csv_path, model_out)
