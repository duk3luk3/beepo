import json
import random

from time import sleep
from pysine import sine

CODEFILE = 'res/code.json'

KOCH_SEQ = 'KMRSUAPTLOWI.NJEF0Y,VG5/Q9ZH38B?427C1D6X'


def load_codetable():
    with open(CODEFILE) as codefile:
        code = json.load(codefile)
        return code


def play_code(code_table, code, fspeed, wpm):
    morse = code_table[code.lower()]
    dit_speed = (1.2/fspeed)
    dah_speed = (3 * dit_speed)
    rest_speed = (1.2/wpm)

    for m in morse:
        if m == '.':
            sine(frequency=800, duration=dit_speed)
        elif m == '-':
            sine(frequency=800, duration= dah_speed)
        sleep(rest_speed)

def koch_letter(letter_span, last=None):
    seq = KOCH_SEQ[:letter_span]
    if last:
        last_idx = seq.index(last)

        def weight(i):
            return 0.5 if i == last_idx else 1

        weights = [weight(i) for i in range(letter_span)]
        return random.choices(seq, weights=weights)[0]
    return random.choice(seq)
