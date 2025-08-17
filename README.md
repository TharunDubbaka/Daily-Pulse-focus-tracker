## Daily Pulse – Focus Score Predictor

A simple Flask web app that predicts your daily focus score based on sleep, study hours, mood, and screen time.

## Features

Predicts focus score using a Linear Regression ML model.

Stores user logs for future predictions.

Clean, responsive HTML/CSS interface.

Fully modular Flask app structure — easy to extend or contribute.

Ready to deploy on Render or Heroku.

## Tech Stack

Backend: Python, Flask

ML: scikit-learn, pandas

Frontend: HTML, CSS

Deployment: Gunicorn (via Render/Heroku)

## Folder Structure

DAILY_PULSE/
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── predictor.py
│ ├── data_handler.py
│ ├── templates/
│ │ └── index.html
│ └── static/
│ └── style.css
├── data/
│ ├── daily_productivity.csv
│ └── user_logs.csv
├── tests/
│ ├── test_predictor.py
│ └── test_data_handler.py
├── requirements.txt
├── Procfile
├── run.py
└── .gitignore

## Installation

Clone the repository from GitHub.

Create a virtual environment and activate it.

Install dependencies using the requirements.txt file.

Run the app locally and open the browser at http://127.0.0.1:5000.

## Usage

Enter your Sleep Hours, Study Hours, Mood Score (1-10), and Screen Time Hours.

Click Predict.

The app will display your predicted focus score and a friendly message:

8 or higher → Highly focused

5 to 7.9 → Average focus

Below 5 → Low focus

## Running Tests

Tests are in the tests/ folder.

test_predictor.py checks ML predictions.

test_data_handler.py verifies user log saving.

Use pytest to run all tests.

## Deployment

Include a Procfile with web: gunicorn run:app.

Push your repository to GitHub and connect to Render or Heroku for live deployment.

## Future Improvements

Use more advanced ML models for better prediction accuracy.

Add graphs and charts to visualize focus trends.

Add user authentication for personalized logs.

Make the UI mobile-friendly.


