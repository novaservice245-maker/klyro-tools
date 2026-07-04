<div align="center">

# ⚡ KLYOR v1.0

### Modern Terminal Multitool · OSINT · Utilities · Rich TUI · Clean Architecture

[![Python](https://img.shields.io/badge/Python-3.11+-00FFFF?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-FF00FF?style=for-the-badge)](LICENSE)
[![Code Quality](https://img.shields.io/badge/Code-Quality-00FF88?style=for-the-badge)]()

<br>

> **⚖️ Educational & authorized use only** — See [DISCLAIMER.md](DISCLAIMER.md)

<br>

---

<br>

## ✦ Overview

**Klyor** is a modern, modular terminal application built with **Python** and **Rich**.

Designed for efficiency, clarity, and extensibility.

| | |
|---|---|
| 🎨 **Themes** | Cyan, Purple, Dark Mode, Professional |
| 🌍 **Bilingual** | Full EN / FR support |
| 🔍 **Smart Search** | Fast, intuitive tool discovery |
| 🧩 **Modular** | Clean architecture, easy to extend |
| ⚡ **Performance** | Lightweight, responsive UI |
| 📊 **Rich Dashboard** | Live monitoring & beautiful output |

<br>

---

## 📁 Architecture

```
klyor/
├── core/               # Core application logic
│   ├── __init__.py
│   ├── app.py         # Main application entry
│   ├── config.py      # Configuration management
│   └── logger.py      # Centralized logging
│
├── modules/           # Feature modules
│   ├── osint/        # OSINT utilities
│   ├── network/      # Network tools
│   ├── utils/        # General utilities
│   └── __init__.py
│
├── ui/                # User interface
│   ├── __init__.py
│   ├── dashboard.py   # Main dashboard
│   ├── theme.py       # Theme system
│   ├── components.py  # UI components
│   └── colors.py      # Color palette
│
├── plugins/           # Plugin system
│   ├── __init__.py
│   └── loader.py      # Plugin loader
│
├── utils/             # Shared utilities
│   ├── __init__.py
│   ├── validators.py  # Input validation
│   ├── helpers.py     # Helper functions
│   └── decorators.py  # Decorators
│
├── config/            # Configuration files
│   ├── settings.json  # User settings
│   └── themes.json    # Theme definitions
│
├── data/              # Runtime data
│   ├── cache.json
│   ├── exports/
│   └── logs/
│
├── assets/            # Static assets
│   ├── logos/
│   ├── banners/
│   └── icons/
│
├── tests/             # Test suite
│   ├── __init__.py
│   ├── test_core.py
│   └── test_ui.py
│
├── main.py            # Entry point
├── requirements.txt   # Dependencies
└── LICENSE            # MIT License
```

<br>

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/novaservice245-maker/klyro-tools.git
cd klyro-tools

# Install dependencies
pip install -r requirements.txt

# Run Klyor
python main.py
```

### System Requirements

| | |
|---|---|
| **Python** | 3.11+ |
| **OS** | Windows, macOS, Linux |
| **Memory** | 512 MB minimum |

<br>

---

## ⌨️ Controls

| Key | Action |
|---|---|
| `↑` `↓` | Navigate |
| `←` `→` | Switch panels |
| `Enter` | Select / Execute |
| `F` | Fuzzy search |
| `Q` | Quit |
| `?` | Help |

<br>

---

## 📦 Dependencies

All core dependencies are included in `requirements.txt`:

- **rich** — Beautiful terminal output
- **requests** — HTTP client
- **dnspython** — DNS queries
- **colorama** — Cross-platform colors

Optional packages available via plugins.

<br>

---

## 📜 License

**MIT License** — See [LICENSE](LICENSE) for details

Inspired by best practices in open-source development.

<br>

---

## 📝 Documentation

- [SETUP.md](docs/SETUP.md) — Detailed installation guide
- [ARCHITECTURE.md](docs/ARCHITECTURE.md) — Code structure & design patterns
- [PLUGINS.md](docs/PLUGINS.md) — How to write plugins
- [CONTRIBUTING.md](CONTRIBUTING.md) — Contribution guidelines

<br>

---

<div align="center">

**Klyor** — Modern. Clean. Extensible.

</div>
