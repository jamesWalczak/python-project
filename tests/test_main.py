"""Tests for the main module."""

import sys
from unittest.mock import MagicMock, patch

from template_python_project.main import (
    get_package_version,
    get_python_version,
    greet,
    load_sample_config,
    main,
    show_available_resources,
)


class TestGreet:
    """Test cases for the greet function."""

    def test_greet_with_name(self) -> None:
        """Test greeting with a specific name."""
        result = greet("Alice")
        assert result == "Hello, Alice! Welcome to the Template Python Project."

    def test_greet_without_name(self) -> None:
        """Test greeting without a name."""
        result = greet()
        assert result == "Hello! Welcome to the Template Python Project."

    def test_greet_with_none(self) -> None:
        """Test greeting with None as name."""
        result = greet(None)
        assert result == "Hello! Welcome to the Template Python Project."

    def test_greet_with_empty_string(self) -> None:
        """Test greeting with empty string."""
        result = greet("")
        assert result == "Hello! Welcome to the Template Python Project."


class TestGetPythonVersion:
    """Test cases for the get_python_version function."""

    def test_get_python_version_format(self) -> None:
        """Test that Python version is returned in correct format."""
        version = get_python_version()
        # Should be in format "major.minor.micro"
        parts = version.split(".")
        assert len(parts) == 3
        assert all(part.isdigit() for part in parts)

    def test_get_python_version_matches_sys_version(self) -> None:
        """Test that the returned version matches sys.version_info."""
        version = get_python_version()
        expected = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        assert version == expected


class TestGetPackageVersion:
    """Test cases for the get_package_version function."""

    def test_get_package_version_returns_string(self) -> None:
        """Test that package version is returned as a string."""
        version = get_package_version()
        assert isinstance(version, str)
        assert len(version) > 0

    def test_get_package_version_format(self) -> None:
        """Test that package version follows semantic versioning pattern."""
        version = get_package_version()
        # Should contain at least one dot for semantic versioning
        # Note: in development, this might be something like "0.1.dev1+g1234567"
        assert "." in version or "dev" in version


class TestMain:
    """Test cases for the main function."""

    @patch("builtins.print")
    def test_main_prints_expected_output(self, mock_print: MagicMock) -> None:
        """Test that main function prints expected content."""
        main()

        # Check that print was called multiple times (more calls due to resources)
        assert mock_print.call_count >= 10

        # Get all the printed messages
        printed_messages = [call.args[0] for call in mock_print.call_args_list]

        # Check for expected content
        assert any("Template Python Project" in msg for msg in printed_messages)
        assert any("Package version:" in msg for msg in printed_messages)
        assert any("Python version:" in msg for msg in printed_messages)
        assert any(
            "Hello! Welcome to the Template Python Project." in msg
            for msg in printed_messages
        )
        assert any("Available resources:" in msg for msg in printed_messages)

    @patch("builtins.print")
    def test_main_includes_versions(self, mock_print: MagicMock) -> None:
        """Test that main function includes both package and Python version information."""
        main()

        printed_messages = [call.args[0] for call in mock_print.call_args_list]

        # Check for package version
        package_version_messages = [
            msg for msg in printed_messages if "Package version:" in msg
        ]
        assert len(package_version_messages) == 1
        package_version_message = package_version_messages[0]
        assert get_package_version() in package_version_message

        # Check for Python version
        python_version_messages = [
            msg for msg in printed_messages if "Python version:" in msg
        ]
        assert len(python_version_messages) == 1
        python_version_message = python_version_messages[0]
        assert get_python_version() in python_version_message


class TestResourceFunctions:
    """Test cases for resource-related functions."""

    def test_load_sample_config(self) -> None:
        """Test loading sample configuration."""
        config = load_sample_config()
        assert isinstance(config, str)
        assert len(config) > 0
        # Should contain TOML content
        assert "app_name" in config or "Could not load config" in config

    @patch("builtins.print")
    def test_show_available_resources(self, mock_print: MagicMock) -> None:
        """Test showing available resources."""
        show_available_resources()

        # Should have printed something about resources
        assert mock_print.call_count > 0
        printed_messages = [call.args[0] for call in mock_print.call_args_list]

        # Check for expected content
        resource_messages = [
            msg for msg in printed_messages if "Available resources:" in msg
        ]
        assert len(resource_messages) >= 1
