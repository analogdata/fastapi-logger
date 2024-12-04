from fastapi import FastAPI
from .middleware.fastapi_logging_middleware import RequestResponseLoggingMiddleware
import os

# Create logs directory if it doesn't exist
os.makedirs("logs/request_response_logs", exist_ok=True)


app = FastAPI()
app.add_middleware(
    RequestResponseLoggingMiddleware,
    log_dir=os.path.join("logs", "request_response_logs"),  # Directory for log files
    max_mbytes=8,  # 8 MB max file size
    backup_count=3,  # Keep up to 3 rotated files
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
