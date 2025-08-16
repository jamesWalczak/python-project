"""Utilities for accessing package resources."""

from importlib import resources
from pathlib import Path
from typing import Any

# Import the main package to get the base reference
import template_python_project


def _get_resource_traversable(subpackage: str = "") -> Any:
    """Get the traversable resource object for the given subpackage."""
    base = resources.files(template_python_project) / "resources"
    if subpackage:
        return base / subpackage
    return base


def get_resource_path(resource_name: str, subpackage: str = "") -> Path:
    """Get the path to a resource file.

    Parameters
    ----------
    resource_name : str
        Name of the resource file
    subpackage : str, optional
        Optional subpackage name (e.g., "templates")

    Returns
    -------
    Path
        Path to the resource file

    Examples
    --------
    >>> config_path = get_resource_path("config.toml")
    >>> sql_path = get_resource_path("create_user_table.sql", "templates")
    """
    resource_dir = _get_resource_traversable(subpackage)
    return Path(str(resource_dir / resource_name))


def read_resource_text(
    resource_name: str, subpackage: str = "", encoding: str = "utf-8"
) -> str:
    """Read a resource file as text.

    Parameters
    ----------
    resource_name : str
        Name of the resource file
    subpackage : str, optional
        Optional subpackage name (e.g., "templates")
    encoding : str, optional
        Text encoding (default: utf-8)

    Returns
    -------
    str
        Content of the resource file as string

    Examples
    --------
    >>> config = read_resource_text("config.toml")
    >>> sql = read_resource_text("create_user_table.sql", "templates")
    """
    resource_dir = _get_resource_traversable(subpackage)
    return str((resource_dir / resource_name).read_text(encoding=encoding))


def read_resource_bytes(resource_name: str, subpackage: str = "") -> bytes:
    """Read a resource file as bytes.

    Parameters
    ----------
    resource_name : str
        Name of the resource file
    subpackage : str, optional
        Optional subpackage name (e.g., "templates")

    Returns
    -------
    bytes
        Content of the resource file as bytes

    Examples
    --------
    >>> data = read_resource_bytes("data.json")
    """
    resource_dir = _get_resource_traversable(subpackage)
    return bytes((resource_dir / resource_name).read_bytes())


def list_resources(subpackage: str = "") -> list[str]:
    """List all resources in the package or subpackage.

    Parameters
    ----------
    subpackage : str, optional
        Optional subpackage name (e.g., "templates")

    Returns
    -------
    list[str]
        List of resource file names

    Examples
    --------
    >>> files = list_resources()
    >>> template_files = list_resources("templates")
    """
    resource_dir = _get_resource_traversable(subpackage)
    return [f.name for f in resource_dir.iterdir() if f.is_file()]
