import pandas as pd
import os
LOG_FILE = "data/user_logs.csv"
def save_user_log(sleep, study, mood, screen, focus_score):
    if not os.path.exists(LOG_FILE):
        pd.DataFrame(columns=['sleep_hours','study_hours','mood_score','screen_time_hours','focus_score'])\
          .to_csv(LOG_FILE, index=False)
    new_row = pd.DataFrame([[sleep, study, mood, screen, focus_score]],
                           columns=['sleep_hours','study_hours','mood_score','screen_time_hours','focus_score'])
    new_row.to_csv(LOG_FILE, mode='a', header=False, index=False)
