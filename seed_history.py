import json
import os

HISTORY_FILE = "prediction_history.json"


def initialize_history():
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            json.dump([], f)


def load_history():
    initialize_history()

    with open(HISTORY_FILE, "r") as f:
        return json.load(f)


def save_prediction(country,
                    life_expectancy,
                    expected_schooling,
                    mean_schooling,
                    gni,
                    score,
                    category):

    history = load_history()

    history.append({
        "country": country,
        "life_expectancy": life_expectancy,
        "expected_schooling": expected_schooling,
        "mean_schooling": mean_schooling,
        "gni": gni,
        "score": round(score,3),
        "category": category
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)