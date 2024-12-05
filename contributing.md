# How to Contribute

## Reporting Issues
- If you find a bug, create an issue on the GitHub repository.
- Provide as much detail as possible, including steps to reproduce the issue and any relevant environment details.

## Suggesting Features
If you have an idea for a new feature or an improvement, create a feature request issue.

## Making Changes
- Follow these steps to make changes to the codebase:
- Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    ```
- Make your changes, including updates to tests and documentation.
- Run the tests to ensure your changes work as expected:
    ```bash
    pytest
    ```

## Writing Tests
- Add or update tests for any new functionality or bug fixes in the tests/ directory.
- Ensure test coverage remains high.

## Submitting a Pull Request
- Push your branch to your forked repository:
    ```bash
    git push origin feature/your-feature-name
    ```
- Create a pull request (PR) to the main branch of the original repository.
- Provide a clear description of the changes in your PR, including the issue it addresses (if applicable).

## Code Style

- Follow PEP 8 for Python code style.
- Use descriptive variable names and add comments where necessary.
- Format your code with black to ensure consistency:
    ```bash
    black .
    ```

## Project Setup

```bash
.
├── CODE_OF_CONDUCT.md
├── LICENSE
├── MANIFEST.in
├── README.md
├── app
│   ├── __init__.py
│   ├── fastapi_ndjson_logger
│   │   ├── __init__.py
│   │   └── fastapi_ndjson_logger.py
│   ├── main.py
│   └── tests
│       ├── __init__.py
│       └── test_logging_middleware.py
├── contributing.md
├── logs
│   └── request_response_logs
│       └── app_log.ndjson
└── requirements.txt
```

## Setting up the project for development

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
from .fastapi_ndjson_logger.fastapi_ndjson_logger import (
    RequestResponseLogging,
)
import os

# Create logs directory if it doesn't exist
os.makedirs("logs/request_response_logs", exist_ok=True)


app = FastAPI()
app.add_middleware(
    RequestResponseLogging,
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