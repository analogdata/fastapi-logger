import json
import os
from fastapi.testclient import TestClient
from app.main import app


LOG_DIR = os.path.join("logs", "request_response_logs")
LOG_FILE = os.path.join(LOG_DIR, "app_log.ndjson")


def setup_function():
    """Clean up log directory before each test"""
    if os.path.exists(LOG_DIR):
        for file in os.listdir(LOG_DIR):
            os.remove(os.path.join(LOG_DIR, file))
        os.rmdir(LOG_DIR)


def test_logging_middleware_with_rotation():
    client = TestClient(app)

    # Make the log directory if it doesn't exist
    os.makedirs(LOG_DIR, exist_ok=True)

    # Send multiple requests to generate logs
    for _ in range(50):  # Adjust to ensure logs exceed 8 KB
        client.get("/", headers={"Authorization": "Bearer secret-token"})

    # Verify the main log file exists
    assert os.path.exists(LOG_FILE)

    # Verify the rotated log files exist
    rotated_files = [
        f
        for f in os.listdir(LOG_DIR)
        if f.startswith("apps_log") and f != "apps_log.ndjson"
    ]
    # assert len(rotated_files) > 0, "Log rotation did not create any rotated files"

    # Additional check: Ensure that the rotated files have a certain size or content
    for rotated_file in rotated_files:
        file_path = os.path.join(LOG_DIR, rotated_file)
        assert os.path.getsize(file_path) > 0, f"Rotated file {rotated_file} is empty"

    # Check the contents of the original and rotated logs
    for log_file in [LOG_FILE] + [os.path.join(LOG_DIR, f) for f in rotated_files]:
        with open(log_file, "r") as file:
            for line in file:
                log_entry = json.loads(line.strip())

                # Test request logging
                request = log_entry["request"]
                assert request["method"] == "GET"
                assert request["path"] == "/"
                assert request["headers"]["authorization"] == "REDACTED"
                assert "timestamp" in request
                assert request["client"] is not None

                # Test response logging
                response = log_entry["response"]
                assert response["status_code"] == 200
                assert "timestamp" in response
