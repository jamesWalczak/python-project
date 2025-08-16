#!/usr/bin/env python3
"""Example script demonstrating how to use resources in the Template Python project.

This script shows various ways to access and use the bundled resources.
"""

import json

from template_python_project.resource_utils import (
    get_resource_path,
    list_resources,
    read_resource_text,
)


def main() -> None:
    """Demonstrate resource usage."""
    print("=== Template Python Project Resources Demo ===\n")

    # List all available resources
    print("1. Available resources:")
    resources = list_resources()
    for resource in resources:
        print(f"   - {resource}")

    print("\n2. Available templates:")
    templates = list_resources("templates")
    for template in templates:
        print(f"   - templates/{template}")

    # Read configuration file
    print("\n3. Configuration file content:")
    config = read_resource_text("config.toml")
    print(config)

    # Read and parse JSON data
    print("\n4. JSON data:")
    json_data = read_resource_text("data.json")
    data = json.loads(json_data)
    print(f"   Welcome message: {data['messages']['welcome']}")
    print(f"   Max retries: {data['settings']['max_retries']}")

    # Read SQL template
    print("\n5. SQL template:")
    sql_template = read_resource_text("create_user_table.sql", "templates")
    print(sql_template[:200] + "..." if len(sql_template) > 200 else sql_template)

    # Get file paths (useful for external tools)
    print("\n6. Resource file paths:")
    config_path = get_resource_path("config.toml")
    print(f"   Config path: {config_path}")

    csv_path = get_resource_path("sample_data.csv")
    print(f"   CSV path: {csv_path}")

    # Read CSV data
    print("\n7. Sample CSV data (first 3 lines):")
    csv_content = read_resource_text("sample_data.csv")
    lines = csv_content.strip().split("\n")
    for line in lines[:3]:
        print(f"   {line}")
    print(f"   ... and {len(lines) - 3} more rows")

    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
