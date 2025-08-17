import os
import pandas as pd
import pytest
from app.datahandler import save_user_log, LOG_FILE

def test_save_user_log(tmp_path):
    test_file = tmp_path / "user_logs.csv"
    original_log = LOG_FILE
    from app import data_handler
    data_handler.LOG_FILE = str(test_file)
    save_user_log(7, 4, 8, 5, 7.5)
    assert os.path.exists(test_file)
    df = pd.read_csv(test_file)
    assert df.shape[0] == 1
    assert "focus_score" in df.columns
    data_handler.LOG_FILE = original_log
