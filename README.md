# Python Project

<!-- Logo placeholder -->
<p align="center">
  <img src="https://via.placeholder.com/200x200?text=Logo" alt="Python Project Logo" width="200"/>
</p>

<!-- Badges -->
<p align="center">
  <a href="https://pypi.org/project/template-python-project/">
    <img src="https://img.shields.io/pypi/v/template-python-project.svg" alt="PyPI version"/>
  </a>
  <a href="https://pypi.org/project/template-python-project/">
    <img src="https://img.shields.io/pypi/pyversions/template-python-project.svg" alt="Python versions"/>
  </a>
  <a href="https://github.com/jamesWalczak/python-project/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/jamesWalczak/python-project.svg" alt="License"/>
  </a>
  <a href="https://github.com/jamesWalczak/python-project/actions">
    <img src="https://github.com/jamesWalczak/python-project/workflows/CI/badge.svg" alt="CI Status"/>
  </a>
  <a href="https://codecov.io/gh/jamesWalczak/python-project">
    <img src="https://codecov.io/gh/jamesWalczak/python-project/branch/main/graph/badge.svg" alt="Coverage"/>
  </a>
  <a href="https://github.com/jamesWalczak/python-project/issues">
    <img src="https://img.shields.io/github/issues/jamesWalczak/python-project.svg" alt="Issues"/>
  </a>
  <a href="https://github.com/jamesWalczak/python-project/stargazers">
    <img src="https://img.shields.io/github/stars/jamesWalczak/python-project.svg" alt="Stars"/>
  </a>
  <a href="https://github.com/jamesWalczak/python-project/network/members">
    <img src="https://img.shields.io/github/forks/jamesWalczak/python-project.svg" alt="Forks"/>
  </a>
</p>

A modern Python project template compatible with Python 3.12 and 3.13.

## Features

- ✅ Modern Python packaging with `pyproject.toml`
- ✅ Src-layout project structure
- ✅ Automatic versioning with setuptools-scm (git-based)
- ✅ Pre-commit hooks for code quality and security
- ✅ Docker support with Ubuntu base image
- ✅ Development tools configuration (Black, isort, mypy, pytest)
- ✅ Security scanning with bandit and detect-secrets
- ✅ MIT License
- ✅ Comprehensive testing setup
- ✅ Type checking with mypy
- ✅ Code formatting with Black
- ✅ Import sorting with isort
- ✅ Docstring linting with pydocstyle

## Project Structure

```
python-project/
├── src/
│   └── template_python_project/
│       ├── __init__.py
│       ├── __main__.py
│       ├── main.py
│       ├── resource_utils.py
│       └── resources/
│           ├── README.md
│           ├── config.toml
│           ├── data.json
│           ├── sample_data.csv
│           └── templates/
│               ├── create_user_table.sql
│               └── welcome_email.txt
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_resource_utils.py
├── examples/
│   ├── __init__.py
│   └── resource_demo.py
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── Makefile
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

## Requirements

- Python 3.12 or 3.13
- pip (latest version recommended)

## Installation

### From source

```bash
git clone https://github.com/jamesWalczak/python-project.git
cd python-project
pip install -e .
```

### For development

```bash
git clone https://github.com/jamesWalczak/python-project.git
cd python-project
pip install -e ".[dev]"
```

## Usage

After installation, you can run the project:

```bash
template_python_project
```

Or run the module directly:

```bash
python -m template_python_project
```

## Resources

The package includes a resources system for bundling configuration files, templates, and data files with your application. Resources are automatically installed with the package and can be accessed using the provided utilities.

### Using Resources

```python
from template_python_project.resource_utils import read_resource_text, list_resources

# Read a configuration file
config = read_resource_text("config.toml")

# Read a template
sql_template = read_resource_text("create_user_table.sql", "templates")

# List available resources
files = list_resources()
templates = list_resources("templates")
```

### Available Resources

- **config.toml** - Default configuration file
- **data.json** - Application data and settings
- **sample_data.csv** - Sample data for testing
- **templates/create_user_table.sql** - SQL template
- **templates/welcome_email.txt** - Email template

See `src/template_python_project/resources/README.md` for detailed documentation.

## Development

### Setup development environment

```bash
# Clone the repository
git clone https://github.com/jamesWalczak/python-project.git
cd python-project

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Running tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_main.py
```

### Code formatting and linting

```bash
# Format code with Black
black src tests

# Sort imports with isort
isort src tests

# Type checking with mypy
mypy src

# Lint with flake8
flake8 src tests

# Security scanning with bandit
bandit -r src

# Check docstrings with pydocstyle
pydocstyle src

# Run all pre-commit hooks
pre-commit run --all-files
```

### Pre-commit Hooks

This project uses pre-commit hooks to maintain code quality. The hooks will run automatically on every commit and include:

- **Code Formatting**: Black, isort
- **Linting**: flake8 with plugins, pydocstyle
- **Type Checking**: mypy
- **Security**: bandit, detect-secrets
- **General**: trailing whitespace, file endings, YAML/JSON validation
- **Python**: pyupgrade for modern syntax

To run hooks manually:
```bash
# Run on all files
make pre-commit

# Run on staged files only
pre-commit run
```

### Docker

Build and run the Docker container:

```bash
# Build the image
docker build -t python-project .

# Run the container
docker run python-project
```

The container will display the Python version and run the application.

## Versioning

This project uses [setuptools-scm](https://github.com/pypa/setuptools_scm) for automatic versioning based on Git tags and commits. The version is determined by:

- Git tags (e.g., `v1.0.0`, `1.0.0`)
- Number of commits since the last tag
- Current commit hash (for development versions)

### Creating a Release

To create a new release:

```bash
# Tag the current commit
git tag v1.0.0
git push origin v1.0.0

# Build the package
python -m build
```

### Version Information

You can check the current version:

```bash
# From command line after installation
python -c "import template_python_project; print(template_python_project.__version__)"

# Or run the main module
python -m template_python_project
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### [0.1.0] - 2025-08-16

- Initial project setup
- Basic project structure
- Docker support
- Development tools configuration
