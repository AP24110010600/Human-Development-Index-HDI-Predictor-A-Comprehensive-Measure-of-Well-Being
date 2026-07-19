"""
Train the HDI Prediction Model
"""

import json
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

from config import (
    DATASET_PATH,
    MODEL_PATH,
    MODEL_META_PATH,
    FEATURE_ORDER
)


def train_model():

    print("Loading dataset...")

    df = pd.read_csv(DATASET_PATH)

    # Remove rows with missing values
    df = df.dropna()

    # Features
    X = df[FEATURE_ORDER]

    # Target
    y = df["HDI"]

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    # Model
    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("Training Complete")
    print("MSE :", mse)
    print("R²  :", r2)

    # Save model
    joblib.dump(model, MODEL_PATH)

    metadata = {
        "model": "RandomForestRegressor",
        "features": FEATURE_ORDER,
        "mse": float(mse),
        "r2_score": float(r2)
    }

    with open(MODEL_META_PATH, "w") as f:
        json.dump(metadata, f, indent=4)

    print("Model saved successfully.")


if __name__ == "__main__":
    train_model()