import pathlib
import requests
from google import genai
from google.genai import types
from typing import Optional
from .config import Config
from .prompts import PromptManager
from .ui import PaimonUI

class PaimonAI:
    """Handles AI communication and file processing"""
    
    def __init__(self, config: Config, prompt_manager: PromptManager):
        self.config = config
        self.prompt_manager = prompt_manager
        self.client = genai.Client(api_key=config.google_api_key)
    
    def chat_with_text(self, user_input: str, prompt_mode: str = "fast") -> str:
        """Chat with AI using text input"""
        system_prompt = self.prompt_manager.get_system_prompt(prompt_mode)
        
        PaimonUI.animate_dots("Paimon is thinking")
        
        response = self.client.models.generate_content(
            model=self.config.model_name,
            contents=f"{system_prompt}\n\nUser: {user_input}",
        )
        return response.text
    
    def chat_with_file(self, file_path: str, prompt: str = "Analyze this file", prompt_mode: str = "fast") -> str:
        """Analyze a file using AI"""
        system_prompt = self.prompt_manager.get_system_prompt(prompt_mode)
        
        PaimonUI.animate_dots("Paimon is uploading and analyzing the file")
        
        # Upload the file
        uploaded_file = self.client.files.upload(file=file_path)
        
        response = self.client.models.generate_content(
            model=self.config.model_name,
            contents=[uploaded_file, f"{system_prompt}\n\nUser: {prompt}"]
        )
        return response.text
    
    def chat_with_image(self, image_path: str, prompt: str = "Analyze this image for OSINT purposes", prompt_mode: str = "fast") -> str:
        """Analyze a local image file using AI"""
        system_prompt = self.prompt_manager.get_system_prompt(prompt_mode)
        
        PaimonUI.animate_dots("Paimon is looking at the image")
        
        # Upload the image
        uploaded_image = self.client.files.upload(file=image_path)
        
        response = self.client.models.generate_content(
            model=self.config.model_name,
            contents=[uploaded_image, f"{system_prompt}\n\nUser: {prompt}"]
        )
        return response.text
    
    def chat_with_url(self, image_url: str, prompt: str = "Analyze this image for OSINT purposes", prompt_mode: str = "fast") -> str:
        """Analyze an image from URL using AI"""
        system_prompt = self.prompt_manager.get_system_prompt(prompt_mode)
        
        PaimonUI.animate_dots("Paimon is downloading and analyzing the image")
        
        # Download image from URL
        response_img = requests.get(image_url, timeout=30)
        response_img.raise_for_status()  # Raises an HTTPError for bad responses
        
        # Determine MIME type based on URL or content
        mime_type = "image/jpeg"  # default
        if image_url.lower().endswith(('.png', '.PNG')):
            mime_type = "image/png"
        elif image_url.lower().endswith(('.gif', '.GIF')):
            mime_type = "image/gif"
        elif image_url.lower().endswith(('.webp', '.WEBP')):
            mime_type = "image/webp"
        
        # Create image part from bytes
        image_part = types.Part.from_bytes(
            data=response_img.content,
            mime_type=mime_type
        )
        
        response = self.client.models.generate_content(
            model=self.config.model_name,
            contents=[f"{system_prompt}\n\nUser: {prompt}", image_part]
        )
        return response.text
    
    @staticmethod
    def is_url(path: str) -> bool:
        """Check if the input is a URL"""
        return path.startswith(('http://', 'https://'))
    
    @staticmethod
    def is_image_file(file_path: str) -> bool:
        """Check if file is an image based on extension"""
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff'}
        return pathlib.Path(file_path).suffix.lower() in image_extensions
    
    def analyze_file(self, file_path: str, prompt: str, mode: str) -> str:
        """Analyze file (image or URL) based on its type"""
        if self.is_url(file_path):
            return self.chat_with_url(file_path, prompt, mode)
        elif self.is_image_file(file_path):
            return self.chat_with_image(file_path, prompt, mode)
        else:
            raise ValueError(f"Unsupported file type. Only image files and URLs are supported. Got: {file_path}")
    
    def analyze_image_url(self, image_url: str, prompt: str, mode: str) -> str:
        """Analyze an image from URL - wrapper for chat_with_url"""
        return self.chat_with_url(image_url, prompt, mode)