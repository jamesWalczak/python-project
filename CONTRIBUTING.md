# Contributing to Python Project

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## Pull Requests

Pull requests are the best way to propose changes to the codebase. We actively welcome your pull requests:

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/python-project.git
   cd python-project
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the project in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

5. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

6. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Code Style

We use several tools to maintain code quality, all configured as pre-commit hooks:

- **Black** for code formatting
- **isort** for import sorting
- **mypy** for type checking
- **flake8** for linting (with additional plugins)
- **pydocstyle** for docstring style
- **bandit** for security scanning
- **detect-secrets** for secret detection
- **pyupgrade** for modern Python syntax
- **pytest** for testing

The pre-commit hooks will run automatically when you commit, but you can also run them manually:

```bash
# Run all hooks on all files
pre-commit run --all-files

# Run all hooks on staged files
pre-commit run

# Run specific hook
pre-commit run black
```

Before submitting a PR, please run:

```bash
# Format code
black src tests
isort src tests

# Type checking
mypy src

# Linting
flake8 src tests

# Run tests
pytest
```

### Code Style Guidelines

- Use type hints for all function parameters and return values
- Write docstrings for all public functions and classes
- Follow PEP 8 style guidelines (enforced by Black and flake8)
- Keep line length to 88 characters (Black default)
- Use meaningful variable and function names

## Testing

- Write tests for all new functionality
- Ensure all tests pass before submitting a PR
- Aim for high test coverage (we use pytest-cov)
- Write both unit tests and integration tests where appropriate

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test
pytest tests/test_main.py::test_function_name
```

## Commit Messages

Write clear, descriptive commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Add user authentication feature

- Implement JWT-based authentication
- Add login and logout endpoints
- Include password hashing utilities
- Add comprehensive test coverage

Fixes #123
```

## Issues

We use GitHub issues to track public bugs. Report a bug by opening a new issue.

### Bug Reports

Great bug reports tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

### Feature Requests

We welcome feature requests! Please:

- Explain the problem you're trying to solve
- Describe the solution you'd like
- Describe alternatives you've considered
- Provide any additional context

## Documentation

- Update README.md if you change functionality
- Add docstrings to new functions and classes
- Update type hints when changing function signatures
- Consider adding examples for new features

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

If you have questions about contributing, please open an issue or reach out to the maintainers.

Thank you for contributing! 🎉
