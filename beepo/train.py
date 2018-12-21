import sys
import morse
import time

from enum import Enum

koch_span = 4
cpm = 15 * 4

morse.play_init()

code_table = morse.load_codetable()
sounds = morse.load_sounds()

letters = morse.KOCH_SEQ[0:koch_span]

for letter in letters:
    print('{0}: {1}'.format(letter, code_table[letter.lower()]))


letter = None

correct_letters = 0
all_letters = 0


class CheckResult(Enum):
    OK = 1
    TOO_SLOW = 2
    WRONG = 3


def check_letter(letter, letter_read, dt):
    if letter.lower() == letter_read.lower():
        if dt <= 60 / cpm:
            return CheckResult.OK
        else:
            return CheckResult.TOO_SLOW
    else:
        return CheckResult.WRONG


while True:
    letter = morse.koch_letter(koch_span, letter)

    morse.play_code(code_table, sounds, letter)

    tm = time.time()

    letter_read = input()

    dt = time.time() - tm

    check_result = check_letter(letter, letter_read, dt)

    all_letters = all_letters + 1

    if check_result == CheckResult.OK:
        print(letter + '.')
        correct_letters = correct_letters + 1
    elif check_result == CheckResult.TOO_SLOW:
        print('{0}... {1} / {2}'.format(letter, dt, 60/cpm))
    else:
        print('{0}!'.format(letter))

    if all_letters % 10 == 0:
        corr_perc = correct_letters / all_letters * 100
        print("Performance: {0}%".format(corr_perc))
