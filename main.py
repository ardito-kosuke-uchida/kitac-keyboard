from random import randrange
from pynput.keyboard import Listener
from playsound import playsound


SOUND_FILE = 'gako.wav'
THRESHOLD = 2500

def on_release(key):
    [lambda: None, lambda: playsound(SOUND_FILE)][randrange(THRESHOLD) == 0]()


with Listener(on_release=on_release) as listener:
    listener.join()
