import sys
import time
from beepo import morse

from functools import partial

from tkinter import *

class Application(Frame):

    def pressed(self, letter):
        print(letter, file=sys.stderr)

        if letter == self.state['current_letter']:
            print('Correct!', file=sys.stderr)
            self.LOG.insert("0.0", "Correct!\n")
        else:
            self.LOG.insert("0.0", f"Incorrect! The letter was {self.state['current_letter']}\n")

        self.after(500, self.next_letter)

    def next_letter(self):
        letter = morse.koch_letter(self.config['koch_span'], self.state['current_letter'])
        print(letter, file=sys.stderr)


        random_letters = morse.random_letters(self.config['koch_span'], len(self.letters), force_letter=letter)
        print(random_letters, file=sys.stderr)

        for i in range(len(random_letters)):
            self.letters[i]["text"] = random_letters[i]
            self.letters[i]["command"] = partial(self.pressed, random_letters[i])

        morse.play_code(self.config['code_table'], self.config['sounds'], letter)

        self.state['current_letter'] = letter

    def start(self):
        print('start!')
        self.next_letter()

    def createLetter(self, frame, col):
        letter = Button(frame, height=20, width=20)
        letter["text"] = "?"
        #letter.pack({"side": "left"})
        letter.grid(row=0, column=col)
        return letter

    def createWidgets(self, config):
        self.config = config

        self.state = {
                'current_letter': None
        }

        self.TOP_FRAME = Frame(self, height=50)
        self.TOP_FRAME.grid(row=0, column=0, sticky=W+E+N+S)

        self.START = Button(self.TOP_FRAME, height=20, width=20)
        self.START["text"] = "START"
        self.START["command"] = self.start
        self.START.grid(row=0, column=0, sticky=W+N+S)

        self.letters = [self.createLetter(self.TOP_FRAME, 1+i) for i in range(config['letter_show'])]

        self.QUIT = Button(self.TOP_FRAME)
        self.QUIT["text"] = "QUIT"
        self.QUIT["command"] = self.quit
        self.QUIT.grid(row=0, column=2+config['letter_show'])

        self.BOTTOM_FRAME = Frame(self)
        self.BOTTOM_FRAME.grid(row=1, column=0)

        self.LOG = Text(self.BOTTOM_FRAME, height=20, width=200)
        self.LOG.pack(fill=BOTH)

    def __init__(self, config, master=None):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=True)
        self.createWidgets(config)

def main():
    morse.play_init()

    config = {
            'group_length': 1,
            'letter_pause': 0.3,
            'koch_span' : 12,
            'letter_show' : 4,
            'cpm' : 15*4,
            'code_table': morse.load_codetable(),
            'sounds': morse.load_sounds()
    }


    root = Tk()
    app = Application(config=config, master=root)
    app.mainloop()
    root.destroy()

if __name__ == "__main__":
    # execute only if run as a script
    main()
