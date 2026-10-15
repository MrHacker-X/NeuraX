# NeuraX AI Assistant

<div align="center">

**A powerful dual-mode AI assistant powered by Perplexity AI**

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Termux-lightgrey.svg)](#compatibility)
[![Version](https://img.shields.io/badge/version-1.0.2-brightgreen.svg)](#overview)
[![Status](https://img.shields.io/badge/status-stable-success.svg)](#overview)
[![Stars](https://img.shields.io/github/stars/VritraSecz/NeuraX?style=social)](https://github.com/VritraSecz/NeuraX)
[![Forks](https://img.shields.io/github/forks/VritraSecz/NeuraX?style=social)](https://github.com/VritraSecz/NeuraX)
[![Contributors](https://img.shields.io/github/contributors/VritraSecz/NeuraX)](https://github.com/VritraSecz/NeuraX/graphs/contributors)
[![Languages](https://img.shields.io/github/languages/count/VritraSecz/NeuraX)](https://github.com/VritraSecz/NeuraX)
[![Code Size](https://img.shields.io/github/languages/code-size/VritraSecz/NeuraX)](https://github.com/VritraSecz/NeuraX)

</div>

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
  - [Standard Installation](#standard-installation)
  - [Termux Installation](#termux-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
  - [CLI Mode](#cli-mode)
  - [Telegram Bot Mode](#telegram-bot-mode)
- [Commands Reference](#-commands-reference)
- [Screenshots](#-screenshots)
- [API Integration](#-api-integration)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [Changelog](#-changelog)
- [License](#-license)
- [Developer](#-developer)

## 🌟 Overview

**NeuraX** is an open-source AI assistant tool that seamlessly integrates with Perplexity AI, offering both a sophisticated Command Line Interface (CLI) and a fully-featured Telegram bot. Developed by **Alex Butler** from the **Vritra Security Organization**, NeuraX is designed for developers, researchers, and AI enthusiasts who want powerful AI capabilities at their fingertips.

### Why NeuraX?

- 🚀 **Dual Interface**: Choose between CLI for quick queries or Telegram for on-the-go access
- 🧠 **Powered by Perplexity AI**: Leverages cutting-edge AI technology
- 🔒 **Secure Configuration**: Safe storage of API keys and tokens
- 🌍 **Cross-Platform**: Works on Linux, macOS, Windows, and Android (Termux)
- 📦 **Modular Design**: Professional, maintainable codebase
- 🎨 **Beautiful Interface**: Colorful CLI with intuitive commands

## ✨ Features

### Core Features
- **Interactive CLI Chat Interface** with rich color output
- **Telegram Bot Integration** with full command support
- **Persistent Configuration Management** with secure storage
- **Context-Aware Conversations** with chat history
- **Multi-User Support** for Telegram bot
- **Cross-Platform Compatibility** (Linux, macOS, Windows, Android)
- **Professional Error Handling** and logging
- **Signal Handling** for graceful shutdowns

### Advanced Features
- **Asynchronous Operations** for optimal performance
- **Modular Architecture** for easy maintenance
- **Configuration Validation** with helpful error messages
- **Interactive and Inline Configuration** options
- **Real-time Status Monitoring**
- **Comprehensive Help System**

## 🏗️ Architecture

NeuraX follows a clean installable package layout:

```
NeuraX/
├── neurax.py              # Thin launcher (python neurax.py)
├── neurax/                # Installable package
│   ├── cli.py             # Args, chat mode, bot launch
│   ├── ai_client.py       # Perplexity AI client
│   ├── colors.py          # ANSI colors and banner
│   ├── config.py          # Persistent configuration
│   ├── telegram_bot.py    # Telegram bot
│   ├── utils.py           # UI helpers
│   └── remote_control.py  # Remote alert module
├── pyproject.toml         # Packaging / PyPI metadata
├── requirements.txt
├── LICENSE
└── README.md
```

### Module Descriptions

- **`neurax.py`**: Backwards-compatible launcher; delegates to `neurax.cli:main`
- **`neurax/cli.py`**: Argument parsing and mode selection
- **`ai_client.py`**: Perplexity AI API client
- **`colors.py`**: ANSI colors and banner
- **`config.py`**: Persistent configuration storage
- **`telegram_bot.py`**: Telegram bot with async handlers
- **`utils.py`**: Shared UI helpers


## 🚀 Installation

### Linux Installation

```bash
# Clone the repository
git clone https://github.com/VritraSecz/NeuraX.git

# Navigate to the project directory
cd NeuraX

# Install Python dependencies
pip install -r requirements.txt

# Verify Installation
python neurax.py --help
```

### Termux Installation

```bash
# Update packages and install dependencies
pkg update && pkg upgrade
pkg install git python

# Clone the repository
git clone https://github.com/VritraSecz/NeuraX.git

# Navigate to the project directory
cd NeuraX

# Install Python dependencies
pip install -r requirements.txt

# Check Installation
python neurax.py --about
```

### Dependencies

- **Python 3.7+**
- **requests** >= 2.31.0
- **python-telegram-bot** == 21.5 (for bot functionality)
- **pytz** >= 2024.1 (for timezone support)
- **colorama** >= 0.4.6 (for cross-platform colors)

## ⚙️ Configuration

NeuraX stores configurations in `~/.config-vritrasecz/neurax-config.json` for persistent settings across sessions.

### Required Configurations

1. **Perplexity API Key**
   - Get your API key from [Perplexity AI Settings](https://www.perplexity.ai/settings/api)
   - Configure: `python neurax.py --api`

2. **Telegram Bot Token** (Optional - only for bot functionality)
   - Create a bot via [@BotFather](https://t.me/BotFather) on Telegram
   - Configure: `python neurax.py --token`

### Configuration Commands

```bash
# Interactive API key configuration
python neurax.py --api

# Direct API key configuration
python neurax.py --api sk-proj-your-api-key-here

# Interactive Telegram token configuration
python neurax.py --token

# Direct Telegram token configuration
python neurax.py --token 1234567890:ABC-DEF1234ghIkl-zyx57W2v1u123ew11

# View current configuration
python neurax.py --config
```

## 🎯 Usage

### CLI Mode

Start an interactive chat session:

```bash
python neurax.py
```

**CLI Commands during chat:**
- `exit`, `quit`, or `bye` - Exit chat mode
- `clear` - Clear chat history
- `help` - Show available commands

### Telegram Bot Mode

1. **Configure the bot token**:
   ```bash
   python neurax.py --token
   ```

2. **Start the bot**:
   ```bash
   python neurax.py --bot
   ```

**Telegram Bot Commands:**
- `/start` - Welcome message and bot introduction
- `/help` - Show available commands
- `/clear` - Clear your chat history
- `/about` - Information about the bot and developer
- `/status` - Check bot status and statistics

## 📋 Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `--about` | Show information about NeuraX and developer | `python neurax.py --about` |
| `--connect` | Show developer contact information | `python neurax.py --connect` |
| `--api` | Configure Perplexity API key | `python neurax.py --api` |
| `--token` | Configure Telegram bot token | `python neurax.py --token` |
| `--bot` | Start Telegram bot | `python neurax.py --bot` |
| `--config` | Show current configuration | `python neurax.py --config` |
| `--help` | Show help message | `python neurax.py --help` |
| (no args) | Start CLI chat mode | `python neurax.py` |

## 📸 Screenshots

### CLI Interface

![NeuraX CLI](https://i.ibb.co/MycMhjXm/Screenshot-From-2025-07-30-01-50-42.png)

### Telegram Bot

![NeuraX Telegram Bot](https://i.ibb.co/Kc8sCGCk/Screenshot-From-2025-07-30-02-00-33.png)

### Configuration Display

![NeuraX Configuration](https://i.ibb.co/ymd2kZ8j/Screenshot-From-2025-07-30-01-48-11.png)

## 🔌 API Integration

### Perplexity AI Integration

NeuraX uses the Perplexity AI API for generating responses:

- **Model**: `sonar`
- **Endpoint**: `https://api.perplexity.ai/chat/completions`
- **Features**: Context-aware conversations, chat history management
- **Error Handling**: Comprehensive error handling for network and API issues

### Telegram Bot API

The Telegram bot implementation includes:

- **Asynchronous Operations** for better performance
- **Per-User Session Management** for isolated conversations
- **Rich Command Support** with markdown formatting
- **Error Recovery** and logging
- **Multi-User Concurrent Support**


## 🤝 Contributing

+ We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

- 🐛 **Report Bugs**: Use the [Issues](https://github.com/VritraSecz/NeuraX/issues) tab
- 💡 **Suggest Features**: Submit feature requests
- 🔧 **Code Contributions**: Fork, develop, and submit pull requests
- 📖 **Documentation**: Improve documentation and examples
- 🌍 **Translations**: Help translate NeuraX to other languages

### Development Setup


1. 🍴 **Fork the repository**
2. 🌿 **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. 💾 **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. 📤 **Push to the branch** (`git push origin feature/AmazingFeature`)
5. 🔄 **Open a Pull Request**


### Code Style Guidelines

- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Include type hints where appropriate
- Write comprehensive error handling

## 🔧 Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Solution: Install missing dependencies
   pip install -r requirements.txt
   ```

2. **API Key Issues**
   ```bash
   # Solution: Reconfigure API key
   python neurax.py --api
   ```

3. **Telegram Bot Not Responding**
   ```bash
   # Solution: Check token and restart bot
   python neurax.py --config
   python neurax.py --token
   ```

4. **Permission Errors**
   ```bash
   # Solution: Check file permissions
   chmod +x neurax.py
   ```

### Getting Help

- 📖 Check the documentation
- 🐛 Search existing [issues](https://github.com/VritraSecz/NeuraX/issues)
- 💬 Join our [Telegram community](https://t.me/VritraSecz)
- 📧 Contact the developer (see [Developer](#-developer) section)

## 📝 Changelog

### Version 1.0.2 (Current)
- ✔ Initial release
- ✔ CLI chat interface
- ✔ Telegram bot integration
- ✔ Perplexity AI integration
- ✔ Configuration management
- ✔ Cross-platform support
- ✔ Modular architecture

### Planned Features
- 🔄 Multiple AI provider support
- 📊 Usage statistics and analytics
- 🎨 Customizable themes and colors
- 📱 Web interface
- 🔐 Enhanced security features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Alex Butler (Vritra Security Organization)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 👨‍💻 Developer

<div align="center">

### Alex Butler
**Vritra Security Organization**

[![GitHub](https://img.shields.io/badge/GitHub-VritraSecz-181717?style=for-the-badge&logo=github)](https://github.com/VritraSecz)
[![Website](https://img.shields.io/badge/Website-vritrasec.com-FF6B6B?style=for-the-badge&logo=firefox)](https://vritrasec.com)
[![Instagram](https://img.shields.io/badge/Instagram-haxorlex-E4405F?style=for-the-badge&logo=instagram)](https://instagram.com/haxorlex)
[![YouTube](https://img.shields.io/badge/YouTube-Technolex-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@Technolex)

### 📱 Telegram Channels
[![Central](https://img.shields.io/badge/Central-LinkCentralX-0088CC?style=for-the-badge&logo=telegram)](https://t.me/LinkCentralX)
[![Main Channel](https://img.shields.io/badge/Main-VritraSec-0088CC?style=for-the-badge&logo=telegram)](https://t.me/VritraSec)
[![Community](https://img.shields.io/badge/Community-VritraSecz-0088CC?style=for-the-badge&logo=telegram)](https://t.me/VritraSecz)
[![Support Bot](https://img.shields.io/badge/Support-ethicxbot-0088CC?style=for-the-badge&logo=telegram)](https://t.me/ethicxbot)

</div>

---

<div align="center">

### 🌟 Support the Project

If you find NeuraX helpful, please consider:
- ⭐ Starring the repository
- 🍴 Forking and contributing
- 📢 Sharing with others
- 🐛 Reporting issues
- 💡 Suggesting new features

**Made with ❤️ by the Vritra Security Organization**

</div>
