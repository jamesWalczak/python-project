# Template Python Project Resources

This directory contains various resource files that are packaged and installed with the Template Python project.

**Note**: This directory intentionally does **NOT** contain `__init__.py` files. This follows Python packaging best practices where resource directories should be data-only, not importable Python modules.

## Best Practices for Resources

### ✅ **DO**: Keep resources as data-only directories
- No `__init__.py` files in resource directories
- Use `importlib.resources` or `importlib_resources` for access
- Separate code from data cleanly

### ❌ **DON'T**: Make resource directories into Python modules
- Don't add `__init__.py` to resource directories
- Don't import resource directories directly
- Don't mix code and data

## Structure

- `config.toml` - Default configuration file
- `data.json` - Application data and settings
- `sample_data.csv` - Sample data for testing and development
- `templates/` - Template files (also data-only, no `__init__.py`)
  - `create_user_table.sql` - SQL template for database setup
  - `welcome_email.txt` - Email template for user onboarding

## Usage

Resources can be accessed in your Python code using the provided utility functions in `resource_utils.py`:

```python
from template_python_project.resource_utils import read_resource_text, list_resources

# Read a text file
config_text = read_resource_text('config.toml')

# Get path to a resource file (for external tools)
csv_path = get_resource_path('sample_data.csv')

# For templates subdirectory
sql_template = read_resource_text('create_user_table.sql', 'templates')
```

### Direct importlib.resources usage (Python 3.9+):

```python
from importlib import resources
import template_python_project

# Read a text file
config_text = (resources.files(template_python_project) / "resources" / "config.toml").read_text()

# Read from subdirectory
sql_template = (resources.files(template_python_project) / "resources" / "templates" / "create_user_table.sql").read_text()
```

## Adding New Resources

1. Add your resource files to this directory or its subdirectories
2. Update the `pyproject.toml` to include them in the package data if needed
3. Document the new resources in this README
4. Add tests to verify the resources are properly included
