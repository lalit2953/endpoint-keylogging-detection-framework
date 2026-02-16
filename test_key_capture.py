from pynput import keyboard

print("Test key capture running...")

def on_press(key):
    print(f"Key pressed: {key}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()