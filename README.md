# GitPush: Automate Your Git Workflow

GitPush is a Python script designed to automate the repetitive task of committing and pushing changes to a Git repository at regular intervals. Whether you're working on a fast-paced project or just want to keep your repository up to date, GitPush simplifies your workflow.

# Getting Started

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.12 (this is what i use, but it may work on older versions as well)
- Git

# Installation

1. Clone this repository to your local machine:
    ```shell
    git clone https://github.com/vrajpat3ll/gitpush.git
    ```

2. Navigate to the project repository:
    ```shell
    cd gitpush
    ```

3. On Windows, run
    ```shell
    ./scripts/build.bat
    ```
3. On Linux, run
    ```shell
    chmod a+x ./scripts/build.sh
    ./scripts/build.sh
    ```
4. Add the executable to PATH for easy access anywhere.

# How to run

```shell
gitpush [-i INTERVAL] [-m MSG]
```
You can run  ```gitpush --help``` or ```gitpush -h``` to get help!

# Next Steps

- _Dynamic Commit Messages_: Integrate AI or allow user input for meaningful commit messages.

- _Error Handling_: Add robust error management.

- _Platform Compatibility_: Ensure smooth execution on Windows, Linux, and macOS.

- _Scheduling Options_: Add functionality to specify custom commit schedules (currently it only works at fixed intervals and cant be changed in between running).

# Contributions

Contributions are welcome! Feel free to submit a pull request or open an issue if you have ideas to improve this project.

