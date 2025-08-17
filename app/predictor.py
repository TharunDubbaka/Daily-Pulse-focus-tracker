import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_focus_score(sleep, study, mood, screen):
    original = pd.read_csv("data/daily_productivity.csv")
    user_logs = pd.read_csv("data/user_logs.csv")
    data = pd.concat([original, user_logs], ignore_index=True)
    X = data[['sleep_hours', 'study_hours', 'mood_score', 'screen_time_hours']]
    y = data['focus_score']
    model = LinearRegression()
    model.fit(X, y)
    prediction = model.predict([[sleep, study, mood, screen]])[0]
    return round(prediction, 2)
