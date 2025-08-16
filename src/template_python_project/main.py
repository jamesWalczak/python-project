"""Main module for the Template Python project.

This module provides the main functionality for the Template Python project,
including version information, greeting functionality, and resource management.
"""

import sys

from . import __version__
from .resource_utils import list_resources, read_resource_text


def get_package_version() -> str:
    """Get the current package version from setuptools-scm.

    Returns
    -------
    str
        A string representation of the package version.
    """
    return __version__


def greet(name: str | None = None) -> str:
    """Generate a greeting message.

    Parameters
    ----------
    name : str or None, optional
        Optional name to greet. If None, uses a default greeting.

    Returns
    -------
    str
        A greeting message string.
    """
    if name:
        return f"Hello, {name}! Welcome to the Template Python Project."
    return "Hello! Welcome to the Template Python Project."


def get_python_version() -> str:
    """Get the current Python version.

    Returns
    -------
    str
        A string representation of the Python version.
    """
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def show_available_resources() -> None:
    """Display available resources in the package."""
    try:
        print("\nAvailable resources:")
        resources = list_resources()
        for resource in resources:
            print(f"  - {resource}")

        print("\nAvailable templates:")
        templates = list_resources("templates")
        for template in templates:
            print(f"  - templates/{template}")
    except Exception as e:
        print(f"Could not list resources: {e}")


def load_sample_config() -> str:
    """Load and return sample configuration.

    Returns
    -------
    str
        Sample configuration as string.
    """
    try:
        return read_resource_text("config.toml")
    except Exception as e:
        return f"Could not load config: {e}"


def main() -> None:
    """Run the main application logic."""
    print("=" * 50)
    print("Template Python Project")
    print("=" * 50)
    print(f"Package version: {get_package_version()}")
    print(f"Python version: {get_python_version()}")
    print(greet())
    print("This is a template Python project with modern tooling.")
    print("Edit src/template_python_project/main.py to add your functionality.")

    # Demonstrate resource loading
    show_available_resources()

    print("\nSample configuration:")
    config = load_sample_config()
    print(config[:200] + "..." if len(config) > 200 else config)
    print("=" * 50)


if __name__ == "__main__":
    main()
