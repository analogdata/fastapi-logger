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

