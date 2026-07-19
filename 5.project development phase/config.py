"""
Configuration settings for the HDI Predictor project.
"""

import os

# ==========================
# Base Directory
# ==========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==========================
# Dataset Path
# ==========================
DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "Human Development Index - Full.csv"
)

# ==========================
# Model Files
# ==========================
MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "model.pkl"
)

MODEL_META_PATH = os.path.join(
    BASE_DIR,
    "model",
    "model_meta.json"
)

# ==========================
# Prediction History
# ==========================
HISTORY_PATH = os.path.join(
    BASE_DIR,
    "history",
    "predictions.json"
)

# ==========================
# Log File
# ==========================
LOG_PATH = os.path.join(
    BASE_DIR,
    "logs",
    "app.log"
)

# ==========================
# Feature Order
# (Update these if your dataset
# uses different column names.)
# ==========================
FEATURE_ORDER = [
    "Life expectancy",
    "Expected years of schooling",
    "Mean years of schooling",
    "GNI per capita"
]

# ==========================
# HDI Category Thresholds
# ==========================
TIER_BANDS = {
    "Very High": (0.800, 1.000),
    "High": (0.700, 0.799),
    "Medium": (0.550, 0.699),
    "Low": (0.000, 0.549)
}

# ==========================
# Flask Secret Key
# ==========================
SECRET_KEY = "HDI_Predictor_2026"