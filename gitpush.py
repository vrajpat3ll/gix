import argparse
import time
from styles import stylise
from voice_listener import listen_for_command
from utils import *
from message import generate_commit_message


def main(args):
    """add, commit and push git changes of the current repo

    Args:
        msg (str): commit message
        interval_seconds (float): time gap in between 2 commits
    """

    clear_screen()
    header()

    commit_msg = args.msg

    if args.mode == "voice":
        listen_for_command(args)
    else:
        start = time.perf_counter()
        stop = False
        while not stop:
            clear_screen()
            header()

            commit_msg = generate_commit_message(args.msg.lower())

            if args.mode == "manual":
                if confirm("Push now?"):
                    git_commit_and_push(commit_msg, args.dry)
            else:
                git_commit_and_push(commit_msg, args.dry)

            # Display time before re-running loop
            interval = args.interval*60 - (time.perf_counter() - start)
            if interval <= 15:
                interval = 15  # 15 second buffer just in case to see the commit message
            while interval > 0:
                start = time.perf_counter()
                print(stylise(
                    f"🎯 Re-running commands in {round(interval, 1)} seconds  ", "cyan"), end='\r')
                interval -= (time.perf_counter() - start)

    return


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["interval", "manual", "voice"],
        default="manual")
    parser.add_argument(
        "-i", "--interval",
        type=float,
        default=5.0,
        help="Interval (minutes) with which you want to add commits | default=5")
    parser.add_argument(
        "-m", "--msg",
        type=str,
        default="default",
        help="Custom commit message for each push | default | auto | default=default"
    )
    parser.add_argument("-y", action='store_true',
                        help='Do not ask for confirmation when trying to push when in voice mode')
    parser.add_argument('--dry', action='store_true',
                        help='Simulate git operations without running them')

    args = parser.parse_args()
    print(args)
    main(args)
