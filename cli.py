import argparse
from .ui import Colors

class PaimonCLI:
    """Handles command line argument parsing and validation"""
    
    def __init__(self):
        self.parser = self._create_parser()
    
    def _create_parser(self) -> argparse.ArgumentParser:
        """Create and configure argument parser"""
        parser = argparse.ArgumentParser(
            description=f'{Colors.PINK}Paimon CLI{Colors.END} - Your magical CTF companion!',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=f"""
{Colors.CYAN}✨ Examples:{Colors.END}
  paimon -t "How do I solve a buffer overflow?"
  paimon --file challenge.py -p "Find the vulnerability"
  paimon -m comprehensive --file binary.exe
  paimon  # Interactive mode with Paimon!

{Colors.PINK}Remember: Paimon is here to help you become the best CTF player!{Colors.END}
            """
        )
        
        # Mode argument
        parser.add_argument('-m', '--mode', 
                           choices=['f', 'c', 'fast', 'comprehensive'],
                           default='f',
                           help='Analysis mode: f/fast for quick help, c/comprehensive for detailed analysis')
        
        # File arguments
        parser.add_argument('--file', 
                           action='append',
                           help='File to analyze (can be used multiple times)')
        
        # Prompt argument
        parser.add_argument('-p', '--prompt',
                           default='Analyze this for CTF challenges',
                           help='Custom prompt for file analysis')
        
        # Text input argument
        parser.add_argument('-t', '--text',
                           help='Text input for direct chat with Paimon')
        
        return parser
    
    def parse_args(self):
        """Parse command line arguments"""
        return self.parser.parse_args()
    
    @staticmethod
    def normalize_mode(mode: str) -> str:
        """Normalize mode argument to standard values"""
        return 'fast' if mode in ['f', 'fast'] else 'comprehensive'