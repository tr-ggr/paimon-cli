#!/usr/bin/env python3
"""
Paimon CLI - Your magical CTF companion!
Main entry point for the application.
"""
from .core import PaimonCore

def main():
    """Main application entry point"""
    app = PaimonCore()
    app.run()

if __name__ == "__main__":
    main()