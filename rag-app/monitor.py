from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import pandas as pd
import os

# Folder to store drift data
DRIFT_DIR = "drift_data"
os.makedirs(DRIFT_DIR, exist_ok=True)

# Save new data & generate report
def log_query_and_check_drift(user_query: str):
    # File where historical data is stored
    history_file = os.path.join(DRIFT_DIR, "query_history.csv")

    # Create new dataframe with current query
    new_data = pd.DataFrame({"query": [user_query]})

    if os.path.exists(history_file):
        # Load historical queries
        ref_data = pd.read_csv(history_file)
        # Run drift report
        report = Report(metrics=[DataDriftPreset()])
        report.run(reference_data=ref_data, current_data=new_data)
        report.save_html(os.path.join(DRIFT_DIR, "query_drift_report.html"))

        # Append new query to history
        ref_data = pd.concat([ref_data, new_data], ignore_index=True)
    else:
        # First-time init
        ref_data = new_data

    ref_data.to_csv(history_file, index=False)
