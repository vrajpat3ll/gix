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
    if args.msg == None:
        # if no message specified, default to this
        args.msg = "auto commit at " + time.asctime()

    # TODO: integrate OpenAI to generate custom commit messages
    elif args.msg.lower() == "gpt":
        while True:
            api_key = input(
                colorise("Please provide OpenAI's API key: ", "yellow"))
            print(f"{api_key = }")
            res = input(colorise("Is this your API key?", "yellow") +
                        f"{api_key} ? [y/n/Enter for y]")
            if res == 'y' or res == '':
                break

    cmds = [
        ["git", "add", "."],
        ["git", "commit", "-m", args.msg],
        ["git", "push"],
    ]

    quit = colorise("<CTRL+C / CMD+C>", "red")

    stop = False
    while not stop:
        if is_windows():
            os.system("cls")
        elif is_linux():
            os.system("clear")

        print(logo)
        print(f"Press {quit} to quit...")

        print("\033[9;1H", end='')
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
        print(colorise())
        time.sleep(args.interval)


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--interval", "-i",
        type=float,
        default=10.0,
        help="Interval with which you want to add commits")

    parser.add_argument(
        "--msg", "-m",
        type=str,
        required=False,
        help="custom commit message for each push"
    )

    args = parser.parse_args()

    main(args)
