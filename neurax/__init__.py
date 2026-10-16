"""NeuraX — CLI and Telegram bot interface for Perplexity AI."""

__version__ = "1.1.0"
__author__ = "Alex Butler"
__email__ = "contact@vritrasec.com"
__url__ = "https://github.com/MrHacker-X/NeuraX"

from .colors import Colors, print_banner
from .config import ConfigManager
from .ai_client import PerplexityAI
from .utils import (
    clear_screen,
    get_input_with_prompt,
    print_about,
    print_connect,
    print_help,
    setup_signal_handler,
)

__all__ = [
    "Colors",
    "print_banner",
    "ConfigManager",
    "PerplexityAI",
    "clear_screen",
    "get_input_with_prompt",
    "print_about",
    "print_connect",
    "print_help",
    "setup_signal_handler",
    "__version__",
]
