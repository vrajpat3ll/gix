from datetime import datetime
import json
import logging
import os
import re
import subprocess as sp
import requests
import json
import re
from datetime import datetime

MAX_RETRIES = 3
# Currently, only ollama models are supported. It works locally on your system.
model = "gemma3"
MODEL_URL = "http://localhost:11434/api/generate"


def is_valid_commit_msg(msg: str) -> bool:
    valid_tags = r"(feat|fix|chore|refactor|docs|test|perf|style)"
    pattern = rf"^{valid_tags}: .{{1,80}}$"
    return re.match(pattern, msg.strip()) is not None and "`" not in msg and "\n" not in msg


def generate_commit_message(seed: str):
    match seed:
        case "default":
            return f"gitpush: commit at {datetime.now().strftime('%H:%M; %b %d, %Y')}"

        case "auto":
            diff = generate_diff('.')  # current repo only
            base_prompt = get_prompt(diff)
            
            for attempt in range(1, MAX_RETRIES + 1):
                payload = {
                    "model": model,
                    "prompt": base_prompt,
                    "stream": True
                }

                commit_msg = ""
                response = requests.post(MODEL_URL, json=payload, stream=True)
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line)
                        commit_msg += data.get("response", "")

                commit_msg = commit_msg.strip()

                if is_valid_commit_msg(commit_msg):
                    return commit_msg
                else:
                    print(f"❗Invalid commit message (attempt {attempt}): {commit_msg}")

            raise ValueError("❌ Failed to generate valid commit message after multiple attempts.")

        case _:
            print("sending custom message", end='\r')
            return seed


def generate_diff(git_repo_base_path: str):
    base_path = os.path.abspath(git_repo_base_path)

    unstaged = sp.run(["git", "diff", "HEAD"], capture_output=True, text=True)
    staged = sp.run(["git", "diff", "--cached"],
                    capture_output=True, text=True)

    full_diff = unstaged.stdout + staged.stdout

    if unstaged.stderr != '' and unstaged.stderr != b'':
        logging.error(f"Couldn't get unstaged diff in repo: {base_path}")
        logging.error(f"{unstaged.stderr}")

    if staged.stderr != '' and staged.stderr != b'':
        logging.error(f"Couldn't get staged diff in repo: {base_path}")
        logging.error(f"{staged.stderr}")

    return full_diff

def get_prompt(diff: str):
    prompt_file = os.path.join( os.path.dirname(os.path.abspath(__file__)), "prompt.txt" )
    # read and insert diff into prompt
    with open(prompt_file, "r") as proompt_file:
        prompt_lines = proompt_file.readlines()
        try:
            diff_index = prompt_lines.index("{DIFF HERE}\n")
        except ValueError:
            try:
                diff_index = prompt_lines.index("{DIFF HERE}")
            except:
                logging.warning("Prompt file must contain a line with exactly '{DIFF HERE}'")
                diff_index = -1
        try:
            url_index = prompt_lines.index("{URL}\n")
        except ValueError:
            try:
                url_index = prompt_lines.index("{URL}")
            except:
                logging.warning("Prompt file must contain a line with exactly '{URL}'")
                url_index = -1

    # with open(os.path.join(os.path.dirname(prompt_file), "README.md"), 'r') as file:
    #     readme = ''.join(file.readlines())
    
    url = sp.run(["git", "config", "--list", "|", "grep", "remote.origin.url"],  capture_output=True, text=True).stdout.removeprefix("remote.origin.url=")
    
    if diff_index != -1: prompt_lines[diff_index] = diff + "\n"
    if url_index != -1: prompt_lines[url_index] = url + "\n"
    prompt = ''.join(prompt_lines)
    
    with open(os.path.join(os.path.dirname(prompt_file), "log_prompt.md"), 'w') as file:
        file.write(prompt)
    return prompt

if __name__ == "__main__":
    print(generate_commit_message("auto"))
