import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for Paimon CLI"""
    
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        self.prompt_file = './prompt.json'
        self.model_name = 'gemini-2.5-flash'
    
    @property
    def google_api_key(self):
        """Get Google API key from environment"""
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        return self.api_key