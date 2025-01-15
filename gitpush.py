import argparse
import os
import subprocess as sp
import time
from colors import colorise, logo

def main(args):
    """add, commit and push git changes of the current repo

    Args:
        msg (str): commit message
        interval_seconds (float): time gap in between 2 commits
    """
    if args.msg == None:
        args.msg = "auto commit at " + time.asctime()

    elif args.msg.lower() == "gpt":
        while True:
            api_key = input(colorise("Please provide OpenAI's API key: ", "yellow"))
            print(f"{api_key = }")
            res = input(colorise("Is this your API key?", "yellow") + f"{api_key} ? [y/n/Enter for y]")
            if res == 'y' or res == '':
                break


    cmds = [
        ["git", "add", "."],
        ["git", "commit", "-m", args.msg],
        ["git", "push"],
    ]

    q = colorise("<CTRL+C / CMD+C>", "red")
    
    # cmds = [
    #     ["git", "status"]
    # ]
    stop = False    
    while not stop:
        os.system("cls")
        print(logo)
        print(f"Press {q} to quit...")

        print("\033[9;1H", end='')
        print(colorise("[TIME] ", "green"), colorise(time.asctime(), "green"), '\n')
        for cmd in cmds:        
            res = sp.run(cmd)
                
            try:
                out = res.stdout
                with open("logs.log", "w+") as f:
                    if out is not None:
                        f.write(str(out))
                        print(out)
                out = res.stderr
                with open("logs.log", "w+") as f:
                    if out is not None:
                        f.write(str(out))
                        print(out)
            except Exception as e:
                print(e)

        time.sleep(args.interval)


if __name__ == "__main__":
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
    print(logo)
    main(args)