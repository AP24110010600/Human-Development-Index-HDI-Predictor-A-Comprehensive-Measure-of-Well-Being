"""
HDI Predictor Flask Application
"""

import webbrowser
from threading import Timer

from flask import Flask, render_template, request

from config import SECRET_KEY
from model_utils import predict_hdi
from seed_history import (
    save_prediction,
    load_history,
    initialize_history
)

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Create history file if it doesn't exist
initialize_history()


def open_browser():
    """Automatically open the application in the default browser."""
    webbrowser.open("http://127.0.0.1:5001")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        country = request.form["country"]

        life_expectancy = float(request.form["life_expectancy"])
        expected_schooling = float(request.form["expected_schooling"])
        mean_schooling = float(request.form["mean_schooling"])
        gni = float(request.form["gni"])

        score, category = predict_hdi(
            life_expectancy,
            expected_schooling,
            mean_schooling,
            gni
        )

        save_prediction(
            country,
            life_expectancy,
            expected_schooling,
            mean_schooling,
            gni,
            score,
            category
        )

        return render_template(
            "result.html",
            country=country,
            score=round(score, 3),
            category=category,
            life_expectancy=life_expectancy,
            expected_schooling=expected_schooling,
            mean_schooling=mean_schooling,
            gni=gni
        )

    except Exception as e:
        import traceback
        traceback.print_exc()

        return render_template(
            "error.html",
            error=str(e)
        )


@app.route("/history")
def history():
    history_data = load_history()

    return render_template(
        "history.html",
        history=history_data
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":

    # Open browser automatically after Flask starts
    Timer(2, open_browser).start()

    app.run(
        host="127.0.0.1",
        port=5001,
        debug=False,
        use_reloader=False
    )