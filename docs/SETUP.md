# Klyor Setup Guide

## System Requirements

- Python 3.11 or higher
- 512 MB RAM minimum
- Internet connection (for some features)

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/novaservice245-maker/klyro-tools.git
cd klyro-tools

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## First Run

```bash
# Run Klyor
python main.py
```

On first run, Klyor will:
1. Create configuration directory (`~/.klyor/`)
2. Create default settings
3. Initialize logging
4. Display main dashboard

## Configuration

Configuration is stored in `~/.klyor/config/settings.json`:

```json
{
  "language": "en",
  "theme": "dark",
  "username": "Operator",
  "skip_boot_animation": false,
  "auto_update": true
}
```

## Troubleshooting

### Module not found error

Ensure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

### Permission denied on Linux/Mac

Make main.py executable:
```bash
chmod +x main.py
```

### Port already in use

Klyor doesn't use network ports, but some plugins might. Check plugin documentation.

## Uninstallation

To remove Klyor:

```bash
# Remove virtual environment
rm -rf venv

# Remove configuration directory
rm -rf ~/.klyor

# Remove repository directory
rm -rf klyro-tools
```
