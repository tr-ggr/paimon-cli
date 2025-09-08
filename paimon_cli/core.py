import os
from typing import List, Optional
from .config import Config
from .ui import PaimonUI, Colors
from .prompts import PromptManager
from .ai_client import PaimonAI
from .cli import PaimonCLI

class PaimonCore:
    """Core application logic coordinator"""
    
    def __init__(self):
        self.config = Config()
        self.prompt_manager = PromptManager()
        self.ai_client = PaimonAI(self.config, self.prompt_manager)
        self.cli = PaimonCLI()
        self.ui = PaimonUI()
    
    def handle_text_input(self, text: str, mode: str):
        """Handle text analysis request"""
        mode_display = self.ui.get_mode_display(mode)
        
        self.ui.print_separator(f"Text Analysis - {mode_display}")
        self.ui.print_paimon_message(f"Let me help you with that! ({mode} mode)", "thinking")
        print()
        
        result = self.ai_client.chat_with_text(text, mode)
        
        self.ui.print_analysis_result("Paimon's Analysis", result)
        self.ui.print_separator()
    
    def handle_file_analysis(self, files: List[str], prompt: str, mode: str):
        """Handle file analysis requests"""
        mode_display = self.ui.get_mode_display(mode)
        
        for i, file_path in enumerate(files):
            if not os.path.exists(file_path):
                self.ui.print_paimon_message(
                    f"Oops! I can't find the file '{file_path}'. Did you spell it right?", 
                    "error"
                )
                continue
            
            file_name = os.path.basename(file_path)
            self.ui.print_separator(f"Analyzing: {file_name} - {mode_display}")
            self.ui.print_paimon_message(f"Time to examine this file! ({mode} mode)", "analyzing")
            print()
            
            try:
                result = self.ai_client.analyze_file(file_path, prompt, mode)
                self.ui.print_analysis_result(f"Paimon's Analysis of {file_name}", result)
                
                if i < len(files) - 1:  # Not the last file
                    print()
                    
            except Exception as e:
                self.ui.print_paimon_message(
                    f"Oops! Something went wrong analyzing {file_name}: {str(e)}", 
                    "error"
                )
            
            self.ui.print_separator()
    
    def handle_interactive_mode(self, mode: str):
        """Handle interactive chat mode"""
        self.ui.print_separator("Interactive Mode")
        self.ui.print_paimon_message("Hi there, Traveler! I'm Paimon, your CTF companion!", "success")
        self.ui.print_paimon_message(f"Currently in {mode} mode. Ask me anything about CTF challenges!", "info")
        self.ui.print_paimon_message("Type 'quit', 'exit', or 'bye' to leave~", "info")
        self.ui.print_separator()
        
        while True:
            try:
                user_input = self.ui.get_user_input()
                
                if user_input.lower() in ['quit', 'exit', 'q', 'bye']:
                    self.ui.print_paimon_message("Aww, leaving so soon? Come back anytime, Traveler!", "success")
                    print(f"{Colors.PINK}✨ May your flags be many and your exploits successful! ✨{Colors.END}")
                    break
                
                if user_input:
                    result = self.ai_client.chat_with_text(user_input, mode)
                    print(f"\n{Colors.BOLD}{Colors.CYAN}✨ Paimon:{Colors.END} {Colors.CYAN}{result}{Colors.END}")
                
            except KeyboardInterrupt:
                print(f"\n{Colors.PINK}✨ Ctrl+C? Okay, bye bye Traveler! ✨{Colors.END}")
                break
            except Exception as e:
                self.ui.print_paimon_message(f"Uh oh! Something went wrong: {str(e)}", "error")
    
    def run(self):
        """Main application entry point"""
        # Clear screen and show banner
        self.ui.clear_screen()
        self.ui.print_banner()
        
        try:
            args = self.cli.parse_args()
            mode = self.cli.normalize_mode(args.mode)
            
            # Handle text input
            if args.text:
                self.handle_text_input(args.text, mode)
            
            # Handle file inputs
            if args.file:
                self.handle_file_analysis(args.file, args.prompt, mode)
            
            # Interactive mode if no arguments provided
            if not args.text and not args.file:
                self.handle_interactive_mode(mode)
                
        except KeyboardInterrupt:
            print(f"\n{Colors.PINK}✨ Goodbye, Traveler! May the winds guide you! ✨{Colors.END}")
        except Exception as e:
            self.ui.print_paimon_message(f"Oh no! A fatal error occurred: {str(e)}", "error")
            self.ui.print_paimon_message("Don't worry, even the best adventurers face challenges!", "info")
    
def main():
    """Entry point for the CLI application"""
    app = PaimonCore()
    app.run()

if __name__ == "__main__":
    main()