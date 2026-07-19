"""
Everything related to the ML model lives here:
- Loading the trained model
- Predicting HDI
- Classifying HDI category
"""

import joblib
import numpy as np

from config import MODEL_PATH

# Load the trained model only once
model = joblib.load(MODEL_PATH)


def predict_hdi(
    life_expectancy,
    expected_years_schooling,
    mean_years_schooling,
    gni_per_capita
):
    """
    Predict HDI score from user inputs.
    """

    features = np.array([[
        life_expectancy,
        expected_years_schooling,
        mean_years_schooling,
        gni_per_capita
    ]])

    score = float(model.predict(features)[0])

    category = classify_hdi(score)

    return score, category


def classify_hdi(score):
    """
    Convert HDI score into development category.
    """

    if score >= 0.800:
        return "Very High Human Development"

    elif score >= 0.700:
        return "High Human Development"

    elif score >= 0.550:
        return "Medium Human Development"

    else:
        return "Low Human Development"