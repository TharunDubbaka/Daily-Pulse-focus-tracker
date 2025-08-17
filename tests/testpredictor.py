import pandas as pd
from app.predictor import predict_focus_score

def test_predict_focus_score(tmp_path):
    data = pd.DataFrame({
        "sleep_hours": [6, 8, 5],
        "study_hours": [3, 5, 2],
        "mood_score": [7, 8, 6],
        "screen_time_hours": [4, 6, 5],
        "focus_score": [7, 8, 5]
    })
    data.to_csv(tmp_path / "daily_productivity.csv", index=False)
    (tmp_path / "user_logs.csv").write_text("sleep_hours,study_hours,mood_score,screen_time_hours,focus_score\n")
    import app.predictor as predictor
    pd.read_csv_orig = pd.read_csv
    def fake_read_csv(path, *args, **kwargs):
        if "daily_productivity" in str(path):
            return data
        elif "user_logs" in str(path):
            return pd.read_csv_orig(tmp_path / "user_logs.csv")
        return pd.read_csv_orig(path, *args, **kwargs)
    pd.read_csv = fake_read_csv

    result = predict_focus_score(7, 4, 8, 5)
    assert isinstance(result, float)
    pd.read_csv = pd.read_csv_orig
