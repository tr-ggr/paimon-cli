import os
import time

PAIMON_TITLE = """
██████╗  █████╗ ██╗███╗   ███╗ ██████╗ ███╗   ██╗     ██████╗██╗     ██╗
██╔══██╗██╔══██╗██║████╗ ████║██╔═══██╗████╗  ██║    ██╔════╝██║     ██║
██████╔╝███████║██║██╔████╔██║██║   ██║██╔██╗ ██║    ██║     ██║     ██║
██╔═══╝ ██╔══██║██║██║╚██╔╝██║██║   ██║██║╚██╗██║    ██║     ██║     ██║
██║     ██║  ██║██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║    ╚██████╗███████╗██║
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝╚══════╝╚═╝
"""

class Colors:
    """Terminal color codes"""
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    PINK = '\033[95m'
    WHITE = '\033[97m'

class PaimonUI:
    """Handles all UI-related functionality for Paimon CLI"""
    
    @staticmethod
    def clear_screen():
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_banner():
        """Print the beautiful Paimon banner"""
        print(Colors.PINK + PAIMON_TITLE + Colors.END)
    
    @staticmethod
    def print_separator(text="", char="═", length=60):
        """Print a pretty separator line"""
        if text:
            padding = (length - len(text) - 2) // 2
            separator = char * padding + f" {text} " + char * padding
            if len(separator) < length:
                separator += char
        else:
            separator = char * length
        print(Colors.PURPLE + separator + Colors.END)
    
    @staticmethod
    def print_paimon_message(message, type="info"):
        """Print message with Paimon-style formatting"""
        icons = {
            "info": "✨",
            "success": "🎉",
            "error": "😱",
            "thinking": "🤔",
            "analyzing": "🔍"
        }
        
        colors = {
            "info": Colors.CYAN,
            "success": Colors.GREEN,
            "error": Colors.RED,
            "thinking": Colors.YELLOW,
            "analyzing": Colors.BLUE
        }
        
        icon = icons.get(type, "✨")
        color = colors.get(type, Colors.CYAN)
        
        print(f"{color}{icon} Paimon says: {message}{Colors.END}")
    
    @staticmethod
    def animate_dots(text, duration=2):
        """Animate loading dots"""
        for i in range(duration * 4):
            dots = "." * (i % 4)
            print(f"\r{Colors.YELLOW}{text}{dots}   {Colors.END}", end="", flush=True)
            time.sleep(0.25)
        print()
    
    @staticmethod
    def get_mode_display(mode):
        """Get formatted display text for analysis mode"""
        if mode == 'fast':
            return f"{Colors.YELLOW}⚡ Fast Mode{Colors.END}"
        else:
            return f"{Colors.PURPLE}🔍 Comprehensive Mode{Colors.END}"
    
    @staticmethod
    def print_analysis_result(title, content):
        """Print analysis result in formatted style"""
        print(f"{Colors.BOLD}{Colors.WHITE}📋 {title}:{Colors.END}")
        print(f"{Colors.CYAN}{content}{Colors.END}")
    
    @staticmethod
    def get_user_input(prompt_text="🎭 You: "):
        """Get user input with formatted prompt"""
        return input(f"\n{Colors.BOLD}{Colors.GREEN}{prompt_text}{Colors.END}").strip()