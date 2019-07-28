import json
import pygame
import random
import os

from time import sleep

CODEFILE = 'res/code.json'

SOUNDFILES = {
        '.': 'oggs/dit.ogg',
        '-': 'oggs/dah.ogg',
        '?': 'oggs/chime.wav',
        '!': 'oggs/error_cropped.ogg'
}

KOCH_SEQ = 'KMRSUAPTLOWI.NJEF0Y,VG5/Q9ZH38B?427C1D6X'

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def load_codetable():
    with open(resource_path(CODEFILE)) as codefile:
        code = json.load(codefile)
        return code


def play_init():
    pygame.mixer.init()


def load_sounds():
    return {k: pygame.mixer.Sound(resource_path(f)) for k, f in SOUNDFILES.items()}


def play_sound(sounds, symbol):
    sounds[symbol].play()
    while pygame.mixer.get_busy() != 0:
        sleep(0.05)


def play_code(code_table, sounds, code):
    morse = code_table[code.lower()]

    for m in morse:
        play_sound(sounds, m)


def koch_letter(letter_span, last=None):
    seq = KOCH_SEQ[:letter_span]
    if last:
        last_idx = seq.index(last)

        def weight(i):
            return 0.5 if i == last_idx else 1

        weights = [weight(i) for i in range(letter_span)]
        return random.choices(seq, weights=weights)[0]
    return random.choice(seq)

def random_letters(letter_span, num_letters, force_letter=None):
    seq = list(KOCH_SEQ[:letter_span])
    if force_letter:
        seq.remove(force_letter)

    choices = random.sample(seq, k=num_letters - len(force_letter))

    choices = choices + [force_letter]

    random.shuffle(choices)

    return choices
