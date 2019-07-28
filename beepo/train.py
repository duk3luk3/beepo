import sys
import morse
import time

from enum import Enum

group_length = 1
letter_pause = 0.3
koch_span = 12
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

streak = 0
best_streak = 0


class CheckResult(Enum):
    OK = 1
    TOO_SLOW = 2
    WRONG = 3


def check_letter(letter, letter_read, dt):
    if letter.lower() == letter_read.lower():
        if dt <= (60 / cpm):
            return CheckResult.OK
        else:
            return CheckResult.TOO_SLOW
    else:
        return CheckResult.WRONG


while True:
    letters = "".join([morse.koch_letter(koch_span, letter) for r in range(group_length)])


    for letter in letters:
        morse.play_code(code_table, sounds, letter)
        time.sleep(letter_pause)


    tm = time.time()

    letter_read = input()

    dt = time.time() - tm

    check_result = check_letter(letters, letter_read, dt)

    all_letters = all_letters + 1

    if check_result == CheckResult.OK:
        streak = streak + 1
        best_streak = max(streak, best_streak)
        print(letters + '.')
        correct_letters = correct_letters + 1
    elif check_result == CheckResult.TOO_SLOW:
        streak = 0
        print('{0}... {1} / {2}'.format(letters, dt, 60/cpm))
        morse.play_sound(sounds, '?')
    else:
        streak = 0
        print('{0}!'.format(letters))
        morse.play_sound(sounds, '!')

    if all_letters % 10 == 0:
        corr_perc = correct_letters / all_letters * 100
        print("Performance: {0}%, Streak: {1} / {2}".format(corr_perc, streak, best_streak))
