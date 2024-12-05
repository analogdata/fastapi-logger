import os
import json
import logging
import datetime
from logging.handlers import RotatingFileHandler
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class RequestResponseLogging(BaseHTTPMiddleware):
    def __init__(
        self,
        app,
        log_dir="app_logs",
        max_mbytes=5,
        backup_count=5,
    ):
        """
        Middleware to log requests and responses with log rotation.
        :param log_dir: Directory to store log files.
        :param max_bytes: Maximum size of a single log file in bytes.
        :param backup_count: Number of rotated log files to keep.
        """
        max_bytes = max_mbytes * 1024 * 1024
        super().__init__(app)

        # Ensure the log directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Set up the logger
        self.logger = logging.getLogger("RequestLogger")
        self.logger.setLevel(logging.INFO)

        # RotatingFileHandler to handle log rotation
        log_file = os.path.join(log_dir, "app_log.ndjson")
        handler = RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
        )
        handler.setFormatter(logging.Formatter("%(message)s"))
        self.logger.addHandler(handler)

    async def dispatch(self, request: Request, call_next):
        request_time = datetime.datetime.now(datetime.timezone.utc)
        request_body = await request.body()

        # Redact sensitive headers
        headers = dict(request.headers)
        if "authorization" in headers:
            headers["authorization"] = "REDACTED"

        # Create a single log entry containing both request and response
        log_entry = {
            "request": {
                "timestamp": request_time.isoformat(),
                "method": request.method,
                "path": request.url.path,
                "query_params": dict(request.query_params),
                "headers": headers,
                "client": request.client.host,
                "request_body": request_body.decode("utf-8") if request_body else None,
            }
        }

        # Call the next middleware or route handler
        response = await call_next(request)

        # Add response data to the same log entry
        log_entry["response"] = {
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "status_code": response.status_code,
        }

        # Log the complete entry as a single JSON object
        self.logger.info(json.dumps(log_entry))

        return response
