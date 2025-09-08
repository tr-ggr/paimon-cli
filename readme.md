# Paimon CLI - AI-Powered Security Analysis Tool

A modular, extensible command-line tool for AI-powered text analysis, file analysis, and security research assistance.

## Quick Start

### Prerequisites

- Python 3.7+
- Google API key (for Gemini AI)

### Installation

1. **Clone or download** the project to your local machine
2. **Navigate to the project directory**:
   ```bash
   cd paimon-cli
   ```
3. **Install dependencies**:
   ```bash
   pip install python-dotenv google-generativeai
   ```
4. **Create a `.env` file** in the project root:

   ```bash
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```

   Replace `your_api_key_here` with your actual Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

5. **Run the application**:
   ```bash
   python main.py
   ```

## Usage Guide

### 🚀 Interactive Mode (Recommended for Beginners)

Start a conversation with the AI assistant:

```bash
python main.py
```

- Type your questions and press Enter
- Type `exit` or `quit` to leave
- Perfect for learning and exploration

### 💬 Quick Text Analysis

Get instant answers without entering interactive mode:

```bash
# Security question
python main.py -t "How do SQL injection attacks work?"

# Programming help
python main.py -t "Explain buffer overflow vulnerabilities"

# General assistance
python main.py --text "What are the OWASP Top 10?"
```

### 📁 File Analysis

Analyze code files, documents, or binaries:

```bash
# Analyze a Python file
python main.py --file script.py

# Analyze with custom prompt
python main.py --file malware.exe -p "Find potential security issues"

# Analyze image files
python main.py --file screenshot.png -p "Describe what you see"
```

### 🔍 Analysis Modes

Choose different analysis approaches:

```bash
# Quick analysis (default)
python main.py --file code.c -m quick

# Comprehensive analysis
python main.py --file binary.exe -m comprehensive

# Security-focused analysis
python main.py --file webapp.py -m security
```

### 📋 Command Reference

```bash
# Show help
python main.py --help

# All options
python main.py [OPTIONS]

Options:
  -t, --text TEXT          Direct text input for analysis
  -f, --file PATH         File to analyze
  -p, --prompt TEXT       Custom prompt for analysis
  -m, --mode MODE         Analysis mode (quick/comprehensive/security)
  -h, --help              Show help message
```

### 💡 Usage Examples

**Learning Security Concepts:**

```bash
python main.py -t "Explain cross-site scripting with examples"
```

**Code Review:**

```bash
python main.py --file vulnerable.php -p "Find security vulnerabilities"
```

**Malware Analysis:**

```bash
python main.py --file suspicious.exe -m comprehensive
```

**Interactive Learning:**

```bash
python main.py
# Then ask: "What is penetration testing?"
```

## Directory Structure

```
paimon-cli/
├── main.py                 # Entry point
├── paimon/                 # Main package
│   ├── __init__.py        # Package initialization
│   ├── config.py          # Configuration management
│   ├── ui.py              # User interface components
│   ├── prompts.py         # Prompt management
│   ├── ai_client.py       # AI integration
│   ├── cli.py             # Command line interface
│   └── core.py            # Core application logic
├── prompt.json            # Prompt configuration file
├── .env                   # Environment variables
└── requirements.txt       # Dependencies
```

## Module Breakdown

### 1. `config.py` - Configuration Management

- **Purpose**: Manages environment variables and application configuration
- **Key Features**:
  - Loads `.env` file
  - Validates API keys
  - Centralizes configuration constants

### 2. `ui.py` - User Interface Components

- **Purpose**: Handles all visual output and terminal formatting
- **Key Features**:
  - Terminal colors and styling
  - Banner display
  - Loading animations
  - Message formatting
  - User input handling

### 3. `prompts.py` - Prompt Management System

- **Purpose**: Manages AI prompts and system messages
- **Key Features**:
  - Loads prompts from JSON
  - Creates default prompts if missing
  - Supports multiple prompt modes
  - Extensible prompt system

### 4. `ai_client.py` - AI Integration Layer

- **Purpose**: Handles all AI communication and file processing
- **Key Features**:
  - Text chat functionality
  - File analysis (regular files)
  - Image analysis
  - File type detection
  - Unified analysis interface

### 5. `cli.py` - Command Line Interface

- **Purpose**: Parses and validates command line arguments
- **Key Features**:
  - Argument parsing
  - Help text generation
  - Input validation
  - Mode normalization

### 6. `core.py` - Core Application Logic

- **Purpose**: Orchestrates all components and handles main workflows
- **Key Features**:
  - Application initialization
  - Request routing
  - Error handling
  - Interactive mode management

### 7. `main.py` - Application Entry Point

- **Purpose**: Simple entry point that starts the application
- **Key Features**:
  - Minimal bootstrap code
  - Clean separation of concerns

## Advanced Usage

### Importing as Library

```python
from paimon import PaimonCore, PaimonAI, Config

# Use as library
config = Config()
ai = PaimonAI(config)
result = ai.chat_with_text("Explain XSS attacks")
print(result)
```

### Custom Prompts

Create your own `prompt.json` to customize AI behavior:

```json
{
  "quick": "Provide a brief analysis of the following...",
  "comprehensive": "Perform a detailed security analysis...",
  "security": "Focus on security vulnerabilities and risks..."
}
```

## Troubleshooting

### Common Issues

**"API key not found" error:**

- Ensure your `.env` file exists and contains `GOOGLE_API_KEY=your_key`
- Verify your API key is valid at [Google AI Studio](https://makersuite.google.com/)

**"Module not found" errors:**

- Run `pip install python-dotenv google-generativeai`
- Ensure you're in the correct directory

**File analysis not working:**

- Check file permissions
- Ensure the file path is correct
- Some file types may not be supported

## Benefits of This Structure

### 1. **Separation of Concerns**

- Each module has a single, well-defined responsibility
- Easy to understand and maintain
- Changes in one area don't affect others

### 2. **Testability**

- Each component can be unit tested independently
- Mock objects can easily replace dependencies
- Clear interfaces between components

### 3. **Extensibility**

- Easy to add new prompt modes
- Simple to extend UI functionality
- New AI models can be integrated easily

### 4. **Maintainability**

- Bug fixes are localized to specific modules
- Code is easier to read and understand
- Documentation is more straightforward

### 5. **Reusability**

- Components can be reused in other projects
- Clear APIs make integration simple
- Modular design supports different use cases

## Contributing

Feel free to contribute by:

- Adding new analysis modes
- Improving error handling
- Extending file type support
- Enhancing the UI/UX

This refactored structure makes your Paimon CLI much more professional, maintainable, and extensible!
