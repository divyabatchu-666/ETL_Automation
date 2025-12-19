import pandas as pd
import os
from datetime import datetime
import pytest

REPORT_DIR = r"C:/Users/divya/AppData/Local/Programs/Python/Python313/file_to_test/Test_Evidences_ETL/Test_Evidences_ETL"
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
REPORT_FILE = os.path.join(REPORT_DIR, f"ETL_Test_Evidence_{timestamp}.xlsx")

test_results = []

@pytest.fixture
def log_result():
    def _log(test_name, status, reason=""):
        test_results.append({
            "Method Name": test_name,
            "Result": status,
            "Failure Reason": reason
        })
    return _log

def pytest_sessionfinish(session, exitstatus):
    os.makedirs(REPORT_DIR, exist_ok=True)
    df = pd.DataFrame(test_results)

    if not df.empty:
        df.to_excel(REPORT_FILE, index=False)
        print(f"\nTest Evidence file successfully generated at:\n{REPORT_FILE}")
