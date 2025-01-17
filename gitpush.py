import argparse
from os import system
import platform
import subprocess as sp
import time
from colors import colorise, logo


def is_windows():
    return platform.system() == "Windows"


def is_linux():
    return platform.system() == "Linux"


# TODO: integrate OpenAI to generate custom commit messages
# TODO: how to handle error messages?  
def main(args):
    """add, commit and push git changes of the current repo

    Args:
        msg (str): commit message
        interval_seconds (float): time gap in between 2 commits
    """

    if is_windows():
        system("cls")
    elif is_linux():
        system("clear")

    quit = colorise("<CTRL+C / CMD+C>", "red")
    colorised_logo = colorise(logo, "cyan")
    print(colorised_logo, end="\n\n")
    print(f"Press {quit} to quit...")

    commit_msg = args.msg
    if args.msg.lower() == "gpt":
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
            system("cls")
        elif is_linux():
            system("clear")

        cmds = [
            ["git", "add", "."],
            ["git", "commit", "-m", commit_msg],
            ["git", "push"],
        ]

        print(colorised_logo, end="\n\n")
        print(f"Press {quit} to quit...")
        print("\033[10;1H", end='')
        print(colorise("[TIME] ", "green"), colorise(
            time.asctime(), "green"), '\n')

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
        default="gpt",
        help="custom commit message for each push | default=gpt"
    )

    args = parser.parse_args()

    main(args)
