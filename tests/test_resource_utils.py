"""Tests for resource utilities."""

from template_python_project.resource_utils import (
    get_resource_path,
    list_resources,
    read_resource_bytes,
    read_resource_text,
)


class TestResourceUtils:
    """Test cases for resource utility functions."""

    def test_list_resources(self) -> None:
        """Test listing resources in the main resources directory."""
        resources = list_resources()
        assert isinstance(resources, list)
        assert len(resources) > 0
        # Check for expected files
        expected_files = ["config.toml", "data.json", "sample_data.csv"]
        for expected_file in expected_files:
            assert expected_file in resources

    def test_list_template_resources(self) -> None:
        """Test listing resources in the templates subdirectory."""
        templates = list_resources("templates")
        assert isinstance(templates, list)
        assert len(templates) > 0
        # Check for expected template files
        expected_templates = ["create_user_table.sql", "welcome_email.txt"]
        for expected_template in expected_templates:
            assert expected_template in templates

    def test_read_resource_text(self) -> None:
        """Test reading a resource file as text."""
        config_content = read_resource_text("config.toml")
        assert isinstance(config_content, str)
        assert len(config_content) > 0
        assert "app_name" in config_content
        assert (
            "Template Python Project" in config_content
            or "Python Project" in config_content
        )

    def test_read_template_resource_text(self) -> None:
        """Test reading a template resource file as text."""
        sql_content = read_resource_text("create_user_table.sql", "templates")
        assert isinstance(sql_content, str)
        assert len(sql_content) > 0
        assert "CREATE TABLE" in sql_content
        assert "users" in sql_content

    def test_read_resource_bytes(self) -> None:
        """Test reading a resource file as bytes."""
        config_bytes = read_resource_bytes("config.toml")
        assert isinstance(config_bytes, bytes)
        assert len(config_bytes) > 0

    def test_get_resource_path(self) -> None:
        """Test getting the path to a resource file."""
        config_path = get_resource_path("config.toml")
        assert str(config_path).endswith("config.toml")

    def test_get_template_resource_path(self) -> None:
        """Test getting the path to a template resource file."""
        sql_path = get_resource_path("create_user_table.sql", "templates")
        assert str(sql_path).endswith("create_user_table.sql")

    def test_read_json_resource(self) -> None:
        """Test reading and parsing JSON resource."""
        import json

        json_content = read_resource_text("data.json")
        data = json.loads(json_content)

        assert isinstance(data, dict)
        assert "messages" in data
        assert "settings" in data
        assert (
            data["messages"]["welcome"] == "Welcome to Python Project!"
            or "Welcome to Template Python Project!" in data["messages"]["welcome"]
        )

    def test_read_csv_resource(self) -> None:
        """Test reading CSV resource."""
        csv_content = read_resource_text("sample_data.csv")
        lines = csv_content.strip().split("\n")

        # Check header
        assert lines[0] == "name,age,city,country"
        # Check we have data rows
        assert len(lines) > 1
        # Check a sample data row
        assert "Alice Johnson" in csv_content
