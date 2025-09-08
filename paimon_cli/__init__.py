"""
Paimon CLI - A magical CTF companion
"""

from .core import PaimonCore
from .config import Config
from .ui import PaimonUI, Colors
from .prompts import PromptManager
from .ai_client import PaimonAI
from .cli import PaimonCLI

__version__ = "1.0.0"
__author__ = "Paimon CLI Team"

# Main components
__all__ = [
    'PaimonCore',
    'Config', 
    'PaimonUI',
    'Colors',
    'PromptManager',
    'PaimonAI',
    'PaimonCLI'
]