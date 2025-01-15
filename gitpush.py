import argparse
import os
import platform
import subprocess as sp
import time
from colors import colorise, logo


def is_windows():
    return platform.system() == "Windows"


def is_linux():
    return platform.system() == "Linux"


def main(args):
    """add, commit and push git changes of the current repo

    Args:
        msg (str): commit message
        interval_seconds (float): time gap in between 2 commits
    """
    # TODO: integrate OpenAI to generate custom commit messages

    commit_msg = args.msg
    if args.msg != None and args.msg.lower() == "gpt":
        while True:
            api_key = input(
                colorise("Please provide OpenAI's API key: ", "yellow"))
            print(f"{api_key = }")
            res = input(colorise("Is this your API key?", "yellow") +
                        f"{api_key} ? [y/n/Enter for y]")
            if res == 'y' or res == '':
                break
        ...

    quit = colorise("<CTRL+C / CMD+C>", "red")

    stop = False
    while not stop:
        if args.msg == None:
            # if no message specified, default to this
            commit_msg = "auto commit at " + time.asctime()

        if is_windows():
            os.system("cls")
        elif is_linux():
            os.system("clear")

        cmds = [
            ["git", "add", "."],
            ["git", "commit", "-m", commit_msg],
            ["git", "push"],
        ]

        print(logo, end="\n\n")
        print(f"Press {quit} to quit...")
        print("\033[10;1H", end='')
        print(colorise("[TIME] ", "green"), colorise(
            time.asctime(), "green"), '\n')

        for cmd in cmds:
            print(colorise("🎯 Running " + " ".join(arg for arg in cmd), "cyan"))
            res = sp.run(cmd)

            try:
                out = res.stdout
                if out is not None:
                    with open("logs.log", "w+") as f:
                        f.write(str(out))
                        print(out)
                out = res.stderr
                if out is not None:
                    with open("logs.log", "w+") as f:
                        f.write(str(out))
                        print(out)
            except Exception as e:
                print(e)

        print(colorise("Completed running commands.", "cyan"))

        time.sleep(args.interval)


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--interval", "-i",
        type=float,
        default=300.0,
        help="Interval (seconds) with which you want to add commits | default=300")

    parser.add_argument(
        "--msg", "-m",
        type=str,
        required=False,
        help="custom commit message for each push"
    )

    args = parser.parse_args()

    main(args)
