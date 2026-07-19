# Human Development Index (HDI) Predictor

## Overview

The Human Development Index (HDI) Predictor is a Flask-based Machine Learning web application that predicts a country's Human Development Index (HDI) score using four development indicators:

- Life Expectancy
- Expected Years of Schooling
- Mean Years of Schooling
- Gross National Income (GNI PPP) per capita

The application classifies countries into:

- Very High Human Development
- High Human Development
- Medium Human Development
- Low Human Development

---

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-Learn
- HTML
- CSS
- JavaScript

---

## Project Structure

```
HDI_Predictor/
│
├── app.py
├── config.py
├── model_utils.py
├── train_model.py
├── seed_history.py
├── requirements.txt
├── README.md
│
├── dataset/
├── history/
├── logs/
├── model/
├── static/
├── templates/
└── utils/
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run

Train the model:

```bash
python train_model.py
```

Run Flask:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5001
```

---

## Features

- HDI Score Prediction
- HDI Category Prediction
- Prediction History
- Responsive Interface
- Error Handling
