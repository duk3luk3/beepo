import sys
import morse
import time

koch_span = 4
cpm=15*4

morse.play_init()

code_table = morse.load_codetable()
sounds = morse.load_sounds()

letters = morse.KOCH_SEQ[0:koch_span]

for letter in letters:
    print('{0}: {1}'.format(letter, code_table[letter.lower()]))


letter = None

correct_letters = 0
all_letters = 0

while True:
    letter = morse.koch_letter(koch_span, letter)

    morse.play_code(code_table, sounds, letter)

    tm = time.time()

    letter_read = input()

    ss = '!'

    if letter.lower() == letter_read.lower():
        dt = time.time() - tm
        if dt <= (60 / cpm):
            ss = '.'
            correct_letters = correct_letters + 1
        else:
            ss = '... {0} / {1}'.format(dt, 60/cpm)
    all_letters = all_letters + 1



    print(letter + ss)

    if all_letters % 10 == 0:
        corr_perc = correct_letters / all_letters * 100
        print("Performance: {0}%".format(corr_perc))

