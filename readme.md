# Paimon CLI - Your Magical CTF & Digital Forensics Companion

A modular, extensible command-line tool designed specifically for Capture The Flag (CTF) competitions and digital forensics investigations. Paimon leverages AI-powered analysis to help security researchers, CTF players, and forensics analysts quickly understand files, analyze artifacts, and solve challenging puzzles.

## Quick Start

### Prerequisites

- Python 3.7+
- Gemini API key (for Gemini AI)

### Installation

1. **Clone or download** the project to your local machine
2. **Navigate to the project directory**:
   ```bash
   cd paimon-cli
   ```
3. **Install dependencies**:
   ```bash
   pip install -e .
   ```
4. **Create a `.env` file** in the project root:

   ```bash
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

   Replace `your_api_key_here` with your actual Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

5. **Run the application**:
   ```bash
   paimon-cli
   ```

## Usage Guide

### 🚀 Interactive Mode (Perfect for CTF Learning)

Start a conversation with your magical CTF assistant:

```bash
paimon-cli
```

- Ask about CTF techniques and strategies
- Get hints for challenge categories
- Type `exit` or `quit` to leave
- Perfect for learning forensics and CTF methodologies

### 💬 Quick Challenge Analysis

Get instant help with CTF challenges without entering interactive mode:

```bash
# Cryptography challenges
paimon-cli -t "I found this hash: 5d41402abc4b2a76b9719d911017c592"

# Web exploitation
paimon-cli -t "How do I find SQL injection in this login form?"

# Binary exploitation
paimon-cli --text "Explain buffer overflow exploitation techniques"
```

### 📁 Forensics File Analysis

Analyze CTF artifacts, evidence files, and challenge materials:

```bash
# Analyze a suspicious binary
paimon-cli --file challenge.exe

# Examine forensics evidence with context
paimon-cli --file evidence.pcap -p "Find network anomalies and suspicious traffic"

# Analyze steganography challenges
paimon-cli --file hidden.png -p "Look for hidden data or steganographic content"
```

### 🔍 CTF Analysis Modes

Choose different analysis approaches for various challenge types:

```bash
# Quick analysis for initial reconnaissance
paimon-cli --file mystery.bin -m quick

# Comprehensive analysis for complex forensics
paimon-cli --file memory.dump -m comprehensive

# Security-focused analysis for exploitation challenges
paimon-cli --file webapp.php -m security

# Cryptography-focused analysis
paimon-cli --file cipher.txt -m crypto

# Forensics-focused analysis
paimon-cli --file evidence.img -m forensics
```

### 📋 CTF Command Reference

```bash
# Show help
paimon-cli --help

# All options for CTF analysis
paimon-cli [OPTIONS]

Options:
  -t, --text TEXT          Direct text input for CTF assistance
  -f, --file PATH         Challenge file or evidence to analyze
  -p, --prompt TEXT       Custom prompt for specific analysis
  -m, --mode MODE         Analysis mode (fast/comprehensive)
  -h, --help              Show help message
```

### 💡 CTF Usage Examples

**Learning CTF Categories:**

```bash
paimon-cli -t "Explain common CTF categories and what to expect"
```

**Forensics Investigation:**

```bash
paimon-cli --file disk.img -p "Perform digital forensics analysis to find hidden files"
```

**Cryptography Challenges:**

```bash
paimon-cli --file encrypted.txt -m crypto
```

**Reverse Engineering:**

```bash
paimon-cli --file binary.elf -p "Help me understand this binary's functionality"
```

**Interactive CTF Learning:**

```bash
paimon-cli
# Then ask: "What tools should I use for memory forensics?"
```

## Directory Structure

```
paimon-cli/
├── paimon_cli/            # Main package
│   ├── __init__.py        # Package initialization
│   ├── config.py          # Configuration management
│   ├── ui.py              # User interface components
│   ├── prompts.py         # CTF-focused prompt management
│   ├── ai_client.py       # AI integration for forensics
│   ├── cli.py             # Command line interface
│   └── core.py            # Core CTF assistant logic
├── main.py                # Entry point
├── prompt.json            # CTF prompt configuration file
├── .env                   # Environment variables
├── pyproject.toml         # Package configuration
└── requirements.txt       # Dependencies
```

## Module Breakdown

### 1. `config.py` - Configuration Management

- **Purpose**: Manages environment variables and CTF tool configuration
- **Key Features**:
  - Loads `.env` file
  - Validates API keys
  - CTF-specific settings

### 2. `ui.py` - CTF-Themed User Interface

- **Purpose**: Handles visual output with CTF-friendly styling
- **Key Features**:
  - Terminal colors and CTF-themed styling
  - Challenge analysis formatting
  - Loading animations for file processing
  - Forensics report formatting

### 3. `prompts.py` - CTF Prompt Management System

- **Purpose**: Manages AI prompts specialized for CTF and forensics
- **Key Features**:
  - CTF category-specific prompts
  - Forensics investigation templates
  - Challenge hint generation
  - Extensible for new CTF categories

### 4. `ai_client.py` - CTF Analysis Engine

- **Purpose**: Handles AI-powered analysis of CTF artifacts
- **Key Features**:
  - CTF challenge consultation
  - Forensics artifact analysis
  - Binary and malware examination
  - Evidence correlation
  - Steganography detection hints

### 5. `cli.py` - CTF Command Interface

- **Purpose**: Parses CTF-specific command line arguments
- **Key Features**:
  - CTF mode selection
  - Challenge file handling
  - Forensics workflow support
  - Competition-friendly options

### 6. `core.py` - CTF Assistant Core

- **Purpose**: Orchestrates CTF challenge solving workflows
- **Key Features**:
  - Challenge categorization
  - Multi-stage analysis
  - CTF methodology guidance
  - Competition timer integration

## Advanced CTF Usage

### CTF Team Collaboration

```python
from paimon_cli import PaimonCore, PaimonAI, Config

# Use as CTF analysis library
config = Config()
ai = PaimonAI(config)
result = ai.analyze_challenge("challenge.bin", "forensics")
print(result)
```

### Custom CTF Prompts

Create your own `prompt.json` for specific CTF competitions:

```json
{
  "crypto": "Analyze this cryptographic challenge, look for common cipher patterns...",
  "forensics": "Perform digital forensics analysis focusing on timeline and artifacts...",
  "web": "Examine for web vulnerabilities including OWASP top 10...",
  "rev": "Reverse engineer this binary, explain functionality and find flags..."
}
```

## CTF Categories Supported

### 🔐 Cryptography

- Hash identification and cracking hints
- Cipher analysis and pattern recognition
- Key recovery guidance
- Cryptographic protocol analysis

### 🔍 Digital Forensics

- Memory dump analysis
- Disk image investigation
- Network packet analysis
- Timeline reconstruction

### 🌐 Web Exploitation

- Vulnerability identification
- Source code review
- SQL injection guidance
- XSS and CSRF analysis

### ⚙️ Reverse Engineering

- Binary analysis assistance
- Disassembly explanation
- Malware behavior analysis
- Obfuscation techniques

### 🔧 Binary Exploitation

- Buffer overflow guidance
- ROP chain assistance
- Memory corruption analysis
- Exploit development hints

## Troubleshooting CTF Challenges

### Common CTF Issues

**"Can't identify file type" error:**

- Use `file` command first: `file challenge.bin`
- Try different analysis modes
- Check for steganography or encoding

**"AI not understanding CTF context":**

- Be specific about the challenge category
- Provide context about the competition
- Use CTF-specific terminology

**"Analysis taking too long":**

- Try quick mode first: `-m quick`
- Break large files into smaller chunks
- Use specific prompts for targeted analysis

## Benefits for CTF Players

### 1. **Challenge Recognition**

- Quickly identify challenge categories
- Understand common CTF patterns
- Get hints without spoiling solutions

### 2. **Learning Acceleration**

- Learn forensics techniques through practice
- Understand exploitation methodologies
- Build CTF-specific knowledge base

### 3. **Team Collaboration**

- Share analysis results with teammates
- Document investigation processes
- Build repeatable forensics workflows

### 4. **Competition Efficiency**

- Faster initial analysis of challenges
- Automated pattern recognition
- Time-saving file examination

## Contributing to Paimon

Help make Paimon the ultimate CTF companion by:

- Adding new CTF category prompts
- Improving forensics analysis capabilities
- Extending challenge recognition patterns
- Contributing CTF-specific tools integration
- Sharing successful challenge solutions

This magical CTF companion grows stronger with every challenge solved! 🎭✨
