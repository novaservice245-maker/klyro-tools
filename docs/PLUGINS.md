# Klyor Plugin Development Guide

## Plugin Structure

Create a new Python file in the `klyor/plugins/` directory:

```python
# klyor/plugins/my_plugin.py

class MyPlugin:
    """My Custom Plugin.
    
    This plugin provides custom functionality.
    """
    
    name = "My Plugin"
    version = "1.0.0"
    author = "Your Name"
    
    def __init__(self):
        pass
    
    def execute(self, args):
        """Execute the plugin."""
        return f"Hello from {self.name}"
```

## Plugin Lifecycle

1. **Discovery**: Plugins are discovered in `klyor/plugins/`
2. **Loading**: `PluginLoader.load_all()` loads all plugins
3. **Initialization**: Plugin `__init__` is called
4. **Execution**: Plugin methods are called by dashboard

## Example: Simple Calculator Plugin

```python
# klyor/plugins/calculator.py

class Calculator:
    """Simple calculator plugin."""
    
    name = "Calculator"
    version = "1.0.0"
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
```

## Plugin API

Plugins have access to:
- Configuration manager
- Logger instance
- Module registry
- UI components

## Best Practices

1. Always include docstrings
2. Add type hints to functions
3. Use logging for debug information
4. Handle exceptions gracefully
5. Follow PEP 8 style guidelines

## Testing Plugins

```python
# In tests/test_plugins.py

from klyor.plugins.my_plugin import MyPlugin

def test_my_plugin():
    plugin = MyPlugin()
    result = plugin.execute(None)
    assert result is not None
```
