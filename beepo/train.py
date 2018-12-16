import sys
import morse

koch_span = 4

morse.play_init()

code_table = morse.load_codetable()
sounds = morse.load_sounds()

letters = morse.KOCH_SEQ[0:koch_span]

for letter in letters:
    print('{0}: {1}'.format(letter, code_table[letter.lower()]))


letter = None

while True:
    letter = morse.koch_letter(koch_span, letter)

    morse.play_code(code_table, sounds, letter)

    letter_read = input()

    print(letter)

