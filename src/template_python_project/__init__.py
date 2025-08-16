"""Python Project - A modern Python project template."""

try:
    from ._version import __version__
except ImportError:
    # Fallback for development installations without setuptools-scm
    try:
        from importlib.metadata import version

        __version__ = version("template_python_project")
    except ImportError:
        # Final fallback - set a default version
        __version__ = "0.1.0.dev"

__author__ = "Your Name"
__email__ = "your.email@example.com"

from .main import main

__all__ = ["main", "__version__"]
