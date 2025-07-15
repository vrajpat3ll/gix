from message import *
import speech_recognition as sr
import time
from utils import *
from styles import *


def listen_for_command(args):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print(stylise(f"[Voice] Listening for '{TRIGGER_PHRASES}'...", "yellow"))

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            clear_screen()

            header()

            try:
                print(stylise("[Voice] Waiting for command...", "yellow"))
                
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = recognizer.recognize_google(audio).lower()
                print(stylise(f"[Voice] Heard: {command}", "yellow"))

                triggered = False
                for trigger in TRIGGER_PHRASES:
                    if trigger in command:
                        triggered = True
                        break
                        
                if triggered:
                    print(stylise("[Voice] Trigger phrase detected.", "yellow"))
                    
                    if args.y or confirm("Did you mean to run git push?"):
                        commit_msg = generate_commit_message(args.msg)
                        while args.y or not confirm(commit_msg):
                            commit_msg = generate_commit_message(args.msg.lower())
                    
                        git_commit_and_push(commit_msg, args.dry)

                    time.sleep(2)  # avoid double triggers
                else:
                    print(stylise("[Voice] No trigger detected.", "yellow"))
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                print(stylise("[Voice] Could not understand audio.", "yellow"))
            except sr.RequestError as e:
                print(stylise(f"[Voice] API error: {e}", "yellow"))
            time.sleep(1.5)
