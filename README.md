# GitPush

***Automate your git workflow with GitPush and focus more on coding!***

GitPush is a tool designed to streamline the process of committing and pushing changes to a Git repository. It offers multiple modes of operation, including manual, interval-based, and voice-activated commits.

---

## Features

* **Manual Commit Mode**: Trigger commits manually when desired.
* **Interval Commit Mode**: Automatically commit and push changes at specified time intervals.
* **Voice-Activated Mode**: Use voice commands to initiate commits and pushes.
* **LLM-Generated Commit Messages**: Leverage LLMs to generate commit messages based on code diffs.
* **Dry Run Mode**: Simulate git operations without making actual changes.
* **Customizable Prompts**: Define your own prompts for LLMs to tailor commit message generation according to your style.

---

## Pre-requisites

Before you begin, ensure the following software is installed on your system:

- **Python 3.12+**
- **Git**, configured with your account
- **[Ollama](https://ollama.com/)** running locally at `http://localhost:11434` with a supported model (e.g. `llama3`, `mistral`, etc.)
- **Microphone input** (for voice mode)
- Internet access (for installing dependencies)

---

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/vrajpat3ll/gitpush.git
   cd gitpush
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

*Note*: Ensure you have Python 3.12 or later installed.

---

## Usage

### Basic Command

```bash
python gitpush.py [options]
```

### Options

- `--mode`: Set the operation mode. Options:

  - `manual`: Manual commit mode.
  - `interval`: Interval-based commit mode.
  - `voice`: Voice-activated commit mode.
- `--interval`: Time interval in minutes for interval mode.
- `-y`: Do not ask for permission to perform git operations in voice **mode**.
- `--dry`: Simulate git operations without executing them.
- `--msg`: Seed for commit message generation. Options:

  - `default`: Use a default commit message.
  - `auto`: Generate commit message using LLM.
  - `<custom_message>`: Use a custom commit message.

### Examples

* **Manual Commit**:
    ```bash
    python gitpush.py --mode manual --msg "Initial commit"
    ```

* **Interval Commit Every 10 Minutes**:
    ```bash
    python gitpush.py --mode interval --interval 600 --msg auto
    ```

* **Voice-Activated Commit**:
    ```bash
    python gitpush.py --mode voice --msg auto
    ```

* **Dry Run**:
    ```bash
    python gitpush.py --msg auto --dry
    ```
---

## Configuration

### Prompt Customization

The `prompt.txt` file defines the prompt used for LLM-based commit message generation. `<DIFF HERE>` placeholder will be replaced with the actual `git diff` output during runtime.

### Model Configuration

Modify the `model` variable in `message.py` to specify the LLM model you wish to use. Ensure the model is compatible with Ollama.

---

## Voice Activation

Voice commands are processed using the `speech_recognition` library.

*Note*: For Linux users, you may need to install portaudio:

```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```



1. **Run in Voice Mode**:

   ```bash
   python gitpush.py --mode voice --msg auto
   ```

The application listens for the word "*jarvis*" to trigger a commit and push operation.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---