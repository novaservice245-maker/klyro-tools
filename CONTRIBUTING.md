# Contributing to Klyor

## Code of Conduct

All contributors are expected to follow the principles of respect, inclusivity, and professionalism.

## Getting Started

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

```bash
# Clone repository
git clone https://github.com/novaservice245-maker/klyro-tools.git
cd klyro-tools

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development tools
pip install pytest black flake8
```

## Code Style

- Follow PEP 8
- Use Black for code formatting
- Use type hints in all functions
- Include docstrings for all classes and functions

## Testing

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_config.py

# Run with coverage
pytest --cov=klyor
```

## Pull Request Process

1. Update documentation if needed
2. Add tests for new functionality
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Request review from maintainers

## Reporting Bugs

Use GitHub Issues to report bugs. Include:
- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior

## Feature Requests

Use GitHub Discussions for feature requests and suggestions.
