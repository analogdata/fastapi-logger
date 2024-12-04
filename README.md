[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

![Logo](https://analogdatagh-readmeimg.s3.ap-south-1.amazonaws.com/logo/pyrestsmall.png)

# FastAPI-Logger

**FastAPI-Logger** is a middleware that provides easy-to-use request and response logging for FastAPI applications. It supports log rotation, custom log directory, and handles sensitive data securely by redacting sensitive headers.

---

## Features

- Logs all incoming requests and outgoing responses.
- Supports log rotation with customizable file size and backup count.
- Handles sensitive data by redacting headers like `Authorization`.
- Outputs logs in JSON format for easy integration with log management tools.
- Flexible configuration for log directory and file size.

---

## Installation

### Prerequisites
- Python 3.11 or higher
- FastAPI framework

## Project Setup

```bash
fastapi-logger/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI entry point
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── fastapi_logging_middleware.py  # Middleware implementation
├── tests/
│   ├── __init__.py
│   ├── test_logging_middleware.py # Unit tests for logging middleware
├── requirements.txt               # Required Python packages
├── README.md                      # Project documentation
├── LICENSE                        # License file
```

Here's how to set up the project:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fastapi-logger.git
```

2. Set up the virtual environment:

```bash
cd fastapi-logger
python -m venv .venv
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate
```

4. Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use FastAPI-Logger in your FastAPI app & configure the parameters,

```python
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

```

Then run the app using `uvicorn app.main:app --reload`

## Configuration Parameters

| Parameter      | Description                                    | Default Value         |
|----------------|------------------------------------------------|-----------------------|
| `log_dir`      | Directory to store log files                  | `app_logs`            |
| `max_mbytes`    | Maximum size of a log file in Mega bytes before rotation | `8` (8 MB) |
| `backup_count` | Number of rotated files to retain             | `5`                   |

## Support

For any questions or issues, feel free to open an issue on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to submit improvements and bug fixes. Also, please see the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Author

[Rajath Kumar K S](https://github.com/analogdata)
