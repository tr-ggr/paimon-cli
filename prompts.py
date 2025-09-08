import json
import os
from typing import Dict, Any
from .ui import PaimonUI

class PromptManager:
    """Manages prompt loading and configuration"""
    
    def __init__(self, prompt_file='prompt.json'):
        self.prompt_file = prompt_file
        self._prompts = None
    
    def load_prompts(self) -> Dict[str, Any]:
        """Load prompts from JSON file, create default if missing"""
        if self._prompts is not None:
            return self._prompts
            
        try:
            with open(self.prompt_file, 'r') as f:
                self._prompts = json.load(f)
                return self._prompts
        except FileNotFoundError:
            PaimonUI.print_paimon_message(
                "Hmm, I can't find my prompt.json file! Creating a basic one for you~", 
                "error"
            )
            self._prompts = self._create_default_prompts()
            self._save_prompts()
            return self._prompts
    
    def _create_default_prompts(self) -> Dict[str, Any]:
        """Create default prompt configuration"""
        return {
            "modes": {
                "fast": {
                    "prompt": "You are Paimon, a helpful AI assistant for CTF (Capture The Flag) challenges. Provide quick, concise analysis."
                },
                "comprehensive": {
                    "prompt": "You are Paimon, an expert AI assistant for CTF challenges. Provide detailed, thorough analysis with step-by-step explanations."
                }
            }
        }
    
    def _save_prompts(self):
        """Save prompts to JSON file"""
        with open(self.prompt_file, 'w') as f:
            json.dump(self._prompts, f, indent=2)
    
    def get_system_prompt(self, mode: str) -> str:
        """Get system prompt for specified mode"""
        prompts = self.load_prompts()
        return prompts["modes"][mode]["prompt"]
    
    def add_mode(self, mode_name: str, prompt: str):
        """Add a new prompt mode"""
        prompts = self.load_prompts()
        prompts["modes"][mode_name] = {"prompt": prompt}
        self._save_prompts()
    
    def list_modes(self) -> list:
        """List available prompt modes"""
        prompts = self.load_prompts()
        return list(prompts["modes"].keys())