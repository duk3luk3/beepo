import json
import pygame
import random

from time import sleep

CODEFILE = 'res/code.json'

SOUNDFILES = {
        '.': 'oggs/dit.ogg',
        '-': 'oggs/dah.ogg',
        '?': 'oggs/chime_cropped.ogg',
        '!': 'oggs/error_cropped.ogg'
}

KOCH_SEQ = 'KMRSUAPTLOWI.NJEF0Y,VG5/Q9ZH38B?427C1D6X'


def load_codetable():
    with open(CODEFILE) as codefile:
        code = json.load(codefile)
        return code


def play_init():
    pygame.mixer.init()


def load_sounds():
    return {k: pygame.mixer.Sound(f) for k, f in SOUNDFILES.items()}


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
