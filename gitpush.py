import argparse
import os
import platform
import subprocess as sp
import time
from colors import colorise, logo


USE_GPT = False


def find_git_repo():
    path = os.getcwd()
    while not os.path.isdir(os.path.join(path, ".git")):
        path = os.path.join(path, "..")
    return os.path.dirname(os.path.join(path, ".git"))


def is_windows():
    return platform.system() == "Windows"


def is_linux():
    return platform.system() == "Linux"


# TODO: integrate OpenAI to generate custom commit messages
# TODO: how to handle error messages of a command?
def main(args):
    """add, commit and push git changes of the current repo

    Args:
        msg (str): commit message
        interval_seconds (float): time gap in between 2 commits
    """

    global USE_GPT
    if is_windows():
        os.system("cls")
    elif is_linux():
        os.system("clear")

    quit = colorise("<CTRL+C / CMD+C>", "red")
    colorised_logo = colorise(logo, "cyan")
    print(colorised_logo, end="\n\n")
    print(f"Press {quit} to quit...")
    print(colorise(f"Working on \"{find_git_repo()}\" repo", "yellow") ,'\n')


    commit_msg = args.msg
    if args.msg.lower() == "gpt":
        USE_GPT = True
        while True:
            api_key = input(
                colorise("Please provide OpenAI's API key: ", "yellow"))
            print(f"{api_key = }")
            res = input(colorise("Is this your API key?", "yellow") +
                        f" {api_key}\n [y/n/Enter for y] ")
            if res == 'y' or res == '':
                break
        ...

    stop = False
    while not stop:
        if args.msg.lower() == "default":
            # if no message specified, default to this
            commit_msg = "auto commit at " + time.asctime()

        if is_windows():
            os.system("cls")
        elif is_linux():
            os.system("clear")

        if USE_GPT:
            ...
            # commit_msg to be changed here each time we need to commit
            # some call to LLM with prompt as `git status` to get a basic commit message

        cmds = [
            ["git", "add", "."],
            ["git", "commit", "-m", commit_msg],
            ["git", "push"],
        ]

        print(colorised_logo, end="\n\n")
        print(f"Press {quit} to quit...")
        print("\033[10;1H", end='')
        print(colorise(f"Working on \"{find_git_repo()}\" repo", "yellow") ,'\n')
        print(colorise("[TIME] ", "green"), colorise(
            time.asctime(), "green"))

        for cmd in cmds:
            print(colorise("🎯 Running " + " ".join(arg for arg in cmd), "cyan"))
            res = sp.run(cmd)

        print(colorise("Completed running commands.", "cyan"))

        time.sleep(args.interval)


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--interval",
        type=float,
        default=300.0,
        help="Interval (seconds) with which you want to add commits | default=300")

    parser.add_argument(
        "-m", "--msg",
        type=str,
        default="default",
        help="custom commit message for each push | default=default"
    )

    args = parser.parse_args()

    main(args)
