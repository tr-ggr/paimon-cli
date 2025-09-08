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
  paimon -t "How do I analyze OSINT data?"
  paimon --url "https://example.com/image.jpg" -p "What can you find in this image?"
  paimon --file image.png -p "Analyze this image for metadata"
  paimon -m comprehensive --url "https://site.com/photo.jpg"
  paimon  # Interactive mode with Paimon!

{Colors.PINK}Remember: Paimon is here to help you with OSINT investigations!{Colors.END}
            """
        )
        
        # Mode argument
        parser.add_argument('-m', '--mode', 
                           choices=['f', 'c', 'fast', 'comprehensive'],
                           default='f',
                           help='Analysis mode: f/fast for quick help, c/comprehensive for detailed analysis')
        
        # URL arguments (replacing file arguments)
        parser.add_argument('--url', 
                           action='append',
                           help='Image URL to analyze for OSINT (can be used multiple times)')
        
        # File arguments (keeping for local image files)
        parser.add_argument('--file', 
                           action='append',
                           help='Local image file to analyze (can be used multiple times)')
        
        # Prompt argument
        parser.add_argument('-p', '--prompt',
                           default='Analyze this image for OSINT purposes',
                           help='Custom prompt for image analysis')
        
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