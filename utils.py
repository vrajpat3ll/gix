import os
import platform
from styles import stylise
import subprocess as sp
import time

TRIGGER_PHRASES = [
    "jarvis",
    "high time to push",
    "push it",
]

logo = r'''   _____   __     __
  / ____| _\ \   / /
 / /     (_)\ \ / /
( (    __| | \ X /
 \ \__/ /| | / /\ \
  \____/ |_|/_/  \_\ '''

colorised_logo = stylise(logo, "cyan")
quit = stylise("<CTRL+C / CMD+C>", "red")


def read_cmds_from_file():
    commands_file = "~/commands/gitpush_commands.txt"
    if is_windows():
        commands_file = 'C:\\commands\\gitpush_commands.txt'
    elif is_linux():
        commands_file = '~/commands/gitpush_commands.txt'
    with open(commands_file, 'r') as cmd_file:
        cmds = cmd_file.readlines()
        cmds = [cmd.strip().split(' ') for cmd in cmds]
    return cmds


def find_git_repo():
    path = os.getcwd()
    while not os.path.isdir(os.path.join(path, ".git")):
        path = os.path.join(path, "..")
    return os.path.dirname(os.path.join(path, ".git"))


def git_commit_and_push(commit_msg, dry_run: bool):
    cmds = [
        ["git", "add", ".",],
        ["git", "commit", "-m", commit_msg,],
        ["git", "push"]]
    for cmd in cmds:
        if dry_run:
            print(stylise("[DRY]", "inverted-gray"), stylise("🎯 Running " +
                  " ".join(arg for arg in cmd), "cyan"), end='\r')
            time.sleep(.8)
            print(stylise("[DRY]", "inverted-gray"), stylise("✅ Ran " +
                  " ".join(arg for arg in cmd) + "    ", "cyan"))
        else:
            print(stylise("🎯 Running " + " ".join(arg for arg in cmd), "cyan"), end='\r')
            res = sp.run(cmd)
            print(stylise("✅ Ran " + " ".join(arg for arg in cmd), "cyan"))


def is_windows():
    return platform.system() == "Windows"


def is_linux():
    return platform.system() == "Linux"


def clear_screen():
    if is_windows():
        os.system("cls")
    elif is_linux():
        os.system("clear")


def header():
    print(colorised_logo, end="\n\n")
    print(f"Press {quit} to quit...")
    print(stylise(f"Working on \"{find_git_repo()}\" repo", "yellow"), '\n')
    print(stylise("[TIME] ", "green"), stylise(time.asctime(), "green"))


def confirm(msg: str):
    print(stylise(f"{msg}", "yellow"), end=' ')
    confirm = input("[Y/n]")
    return confirm.lower() in ['', 'y']
