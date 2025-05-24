from datetime import datetime
import json
import logging
import os
import requests
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

            # Read and insert diff into prompt
            with open("prompt.txt", "r") as prompt_file:
                prompt_lines = prompt_file.readlines()
                try:
                    diff_index = prompt_lines.index("<DIFF HERE>\n")
                except ValueError:
                    try:
                        diff_index = prompt_lines.index("<DIFF HERE>")
                    except:
                        ...
                    raise ValueError("Prompt file must contain a line with exactly '<DIFF HERE>'")

                prompt_lines[diff_index] = diff + "\n"
                base_prompt = ''.join(prompt_lines)

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
        return ''

    if staged.stderr != '' and staged.stderr != b'':
        logging.error(f"Couldn't get staged diff in repo: {base_path}")
        logging.error(f"{staged.stderr}")
        return ''

    return full_diff


if __name__ == "__main__":
    print(generate_commit_message("auto"))
