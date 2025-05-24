# GitPush - Automated Git Workflow Tool

## Description
GitPush is a powerful command-line tool designed to automate and streamline your Git workflow. It handles git add, commit, and push operations with configurable settings, intelligent commit message generation, and even voice command capabilities. This tool is perfect for developers who want to simplify their version control process and maintain consistent commit practices.

## Features
- **Multiple Operation Modes**:
  - **Manual Mode**: Manually confirm each push operation
  - **Interval Mode**: Automatically commit and push changes at specified time intervals
  - **Voice Mode**: Use voice commands to trigger git operations
- **AI-Generated Commit Messages**: Integration with Ollama to generate contextual and conventional commit messages based on your code changes
- **Cross-Platform Support**: Works on both Windows and Linux systems
- **Customizable Commit Intervals**: Set your preferred time interval between automatic commits
- **Voice Recognition**: Trigger git operations using voice commands
- **Styled Terminal Output**: Colorful and informative terminal interface
- **Custom Command Configuration**: Define your own git commands sequence

## Installation

### Prerequisites
- Python 3.10 or higher
- Git installed and configured
- Ollama (optional, for AI-generated commit messages)

### Steps
1. Clone the repository or download the source code
   ```
   git clone <repository-url>
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. (Optional) Install Ollama for AI-generated commit messages
   - Follow installation instructions at [Ollama's official website](https://ollama.ai/)
   - Ensure Ollama is running with the Gemma model

## Usage

### Basic Usage
```
python gitpush.py
```

### Different Modes

#### Manual Mode (Default)
Asks for confirmation before executing git commands
```
python gitpush.py --mode manual
```

#### Interval Mode
Automatically commits and pushes at specified intervals
```
python gitpush.py --mode interval --interval 10
```

#### Voice Mode
Listen for voice commands to trigger git operations
```
python gitpush.py --mode voice
```
When in voice mode, say "habibi push it" clearly, and the tool will prompt you to confirm before pushing.

## Command-line Arguments

| Argument | Short | Description | Default |
|----------|-------|-------------|---------|
| `--mode` | | Operation mode (`manual`, `interval`, `voice`) | `manual` |
| `--interval` | `-i` | Time interval between commits in minutes | `5.0` |
| `--msg` | `-m` | Commit message | `default` |

### Commit Message Options
- `default`: Uses "gitpush: auto [timestamp]"
- `auto`: Generates commit message using Ollama based on diff
- Custom message: Any string you provide

## Dependencies
- `requests`: For API communication with Ollama
- `SpeechRecognition`: For voice command recognition
- `PyAudio`: Audio processing for voice recognition
- `Ollama` (external): For AI-generated commit messages

## Setup Instructions

### Command File Setup
GitPush reads git commands from a file. Create a commands file at:
- Windows: `C:\commands\gitpush_commands.txt`
- Linux: `~/commands/gitpush_commands.txt`

Format each command on a new line. Use `$msg` as a placeholder for the commit message:
```
git add .
git commit -m $msg
git push
```

### Voice Recognition Setup
1. Ensure you have a working microphone
2. Install the required dependencies:
   ```
   pip install SpeechRecognition PyAudio
   ```
3. Run GitPush in voice mode
4. Use the trigger phrase "habibi push it"

### AI-Generated Commit Messages
1. Install and run Ollama
2. Ensure the Gemma model is available
3. Use `--msg auto` or set to "auto" when running GitPush

## Notes & Requirements

- **Python Version**: Python 3.10+ required for match-case syntax
- **Environment Variables**: Ensure Python is in your system PATH
- **Permissions**: The tool requires permissions to execute git commands
- **Voice Recognition**: Requires an internet connection for Google's speech recognition service
- **AI Integration**: Ollama must be running locally on the default port (11434) for AI-generated commit messages
- **Platform Support**: Tested on Windows and Linux (may work on macOS but not specifically tested)

## License
This project is open source and available under the [MIT License](LICENSE).

