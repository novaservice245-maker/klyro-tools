# Klyor Architecture

## Overview

Klyor follows a modular, layered architecture designed for extensibility and maintainability.

## Core Components

### Application Layer (`klyor/core/`)

- **app.py**: Main application orchestrator
- **config.py**: Configuration management
- **logger.py**: Centralized logging

### Module System (`klyor/modules/`)

Organized by functionality:
- **osint/**: Open Source Intelligence tools
- **network/**: Network utilities
- **utilities/**: General purpose tools

### User Interface (`klyor/ui/`)

- **dashboard.py**: Main dashboard
- **theme.py**: Theme management
- **colors.py**: Color palettes
- **components.py**: Reusable UI components

### Plugin System (`klyor/plugins/`)

- **loader.py**: Dynamic plugin loading

### Utilities (`klyor/utils/`)

- **validators.py**: Input validation
- **helpers.py**: Helper functions
- **decorators.py**: Function decorators

## Design Patterns

### Singleton Pattern
Used for configuration and logger instances.

### Registry Pattern
Modules and plugins are registered in central registries.

### Decorator Pattern
UI components are built using decorators.

## Data Flow

```
User Input
    ↓
[Dashboard]
    ↓
[Module Registry]
    ↓
[Specific Module]
    ↓
Result → [Dashboard] → User
```

## Extension Points

1. **Custom Modules**: Create new module directories under `klyor/modules/`
2. **Plugins**: Drop Python files in `klyor/plugins/`
3. **Themes**: Add color schemes in `klyor/ui/colors.py`
4. **Decorators**: Add custom decorators in `klyor/utils/decorators.py`
