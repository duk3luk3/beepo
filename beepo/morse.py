import json
import pygame
import random

from time import sleep

CODEFILE = 'res/code.json'

DITFILE = 'oggs/dit.ogg'
DAHFILE = 'oggs/dah.ogg'

KOCH_SEQ = 'KMRSUAPTLOWI.NJEF0Y,VG5/Q9ZH38B?427C1D6X'

def load_codetable():
    with open(CODEFILE) as codefile:
        code = json.load(codefile)
        return code

def play_init():
    pygame.mixer.init()

def load_sounds():
    dit = pygame.mixer.Sound(DITFILE)
    dah = pygame.mixer.Sound(DAHFILE)

    return {
            'dit': dit,
            'dah': dah
    }

def play_code(code_table, sounds, code):
    morse = code_table[code.lower()]

    for m in morse:
        if m == '.':
            sounds['dit'].play()
        elif m == '-':
            sounds['dah'].play()
        while pygame.mixer.get_busy() != 0:
            sleep(0.05)

def koch_letter(letter_span, last=None):
    seq = KOCH_SEQ[:letter_span]
    if last:
        last_idx = seq.index(last)
        weights = [(lambda i: 0.5 if i == last_idx else 1)(i) for i in range(letter_span)]
        return random.choices(seq, weights=weights)[0]
    return random.choice(seq)

