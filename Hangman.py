from tkinter import *
from tkinter import ttk
from random import choice

root = Tk()

#WORDS = ['python', 'tkinter', 'hangman', 'game', 'programming']
WORDS = ['PYTHON', 'TKINTER', 'HANGMAN', 'GAME', 'PROGRAMMING', 'KLINGON', 'SCHRODINGER', 'NERD', 'GEEK', 'TRIBBLE', 'WOOKIE', 'JABBA', 'ROBOT', 'DARTHVADER', 'SKYNET', 'QUANTUM', 'GIGAWATT', 'CAPACITOR', 'HOBBIT', 'MUGGLE', 'DEATHSTAR', 'LIGHTSABER', 'PIXEL', 'COOKIE', 'SPAM', 'FRODO', 'MATRIX', 'GANDALF', 'BUTTERFLY', 'FIREWALL', 'CRYPTO', 'BITCOIN', 'DOGECOIN', 'FACTORIAL', 'FIBONACCI', 'ZOMBIE', 'RASPBERRY', 'INCEPTION', 'HYPERSPACE', 'PORTAL', 'GLITCH', 'ALGORITHM', 'DEBUGGING', 'FUNCTION', 'VARIABLE', 'RECURSION', 'DATABASE', 'SERVER', 'CLIENT', 'COMPILE', 'JAVASCRIPT', 'BOOTSTRAP', 'INHERITANCE', 'POLYMORPHISM', 'ENCAPSULATION', 'REPOSITORY', 'BIGDATA', 'REGRESSION', 'PREDICTION']

class Hangman:
    def __init__(self, master):
        self.master = master
        self.master.title("GW Hangman")

        self.hangman_canvas = Canvas(master, width=400, height=400)
        self.hangman_canvas.pack()

        self.word_to_guess = choice(WORDS)
        self.guesses = ['_'] * len(self.word_to_guess)
        self.attempts = 10

        self.lbl_word = ttk.Label(master, text = ' '.join(self.guesses), font=('Lucida 40'))
        self.lbl_word.pack()
        
        self.lbl_attempts = ttk.Label(master, text = f'Attempts left: {self.attempts}', font=('Lucida 18'))
        self.lbl_attempts.pack(pady=18)
        
        self.buttons_frame = ttk.Frame(master)
        self.buttons_frame.pack()

        style = ttk.Style()
        style.configure("BW.TButton", font = ('Lucida 12 bold'))
        style.configure("Large.TButton", font = ('Lucida 16'))

        #alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        rows = [alphabet[i:i+9] for i in range(0, len(alphabet), 9)]
        for row in rows:
            frame = ttk.Frame(self.buttons_frame)
            frame.pack()
            for letter in row:
                button = ttk.Button(frame, text = "\n"+letter+"\n", style="BW.TButton", command=lambda letter=letter: self.guess(letter))
                button.pack(side='left')


        self.guess(self.word_to_guess[-1])
        self.guess(self.word_to_guess[0])

    def draw_hangman(self):
        if self.attempts == 9:
            self.hangman_canvas.create_line(100, 360, 360, 360, width=4)
        if self.attempts == 8:
            self.hangman_canvas.create_line(100, 360, 100, 60, width=4)
        if self.attempts == 7:
            self.hangman_canvas.create_line(100, 60, 250, 60, width=4)
        if self.attempts == 6:
            self.hangman_canvas.create_oval(220, 120, 280, 180, width=4)
        if self.attempts == 5:
            self.hangman_canvas.create_line(250, 180, 250, 290, width=4)
        if self.attempts == 4:
            self.hangman_canvas.create_line(250, 210, 190, 180, width=4)
        if self.attempts == 3:
            self.hangman_canvas.create_line(250, 210, 310, 180, width=4)
        if self.attempts == 2:
            self.hangman_canvas.create_line(250, 290, 310, 320, width=4)
        if self.attempts == 1:
            self.hangman_canvas.create_line(250, 290, 190, 320, width=4)
        if self.attempts == 0:
            self.hangman_canvas.create_line(250, 60, 250, 120, width=4)

    def guess(self, letter):            
        if letter in self.word_to_guess:
            for i, l in enumerate(self.word_to_guess):
                if l == letter:
                    self.guesses[i] = letter
                    self.lbl_word['text'] = ' '.join(self.guesses)
                    if '_' not in self.guesses:
                        #self.win()
                        self.master.after(1, self.win)
        else: 
            self.attempts -= 1
            self.draw_hangman()
        self.lbl_attempts['text'] = f'Attempts left: {self.attempts}'
        if self.attempts == 0:
            self.lose()
            
        for button in self.buttons_frame.winfo_children():
            for b in button.winfo_children():
                if b['text'] == "\n" + letter + "\n":
                    b['state'] = 'disabled'

    def win(self):
        self.lbl_attempts['text'] = 'You win!'
        self.lbl_attempts.configure(foreground='green')
        for button in self.buttons_frame.winfo_children():
            for b in button.winfo_children():
                b['state'] = 'disabled'

    def lose(self):
        self.lbl_attempts['text'] = 'You lose!'
        self.lbl_attempts.configure(foreground='red')
        for button in self.buttons_frame.winfo_children():
            for b in button.winfo_children():
                b['state'] = 'disabled'

def start_new_game():
        for widget in root.winfo_children():
            if not isinstance(widget, ttk.Button):
                widget.destroy()
        Hangman(root)

new_game_button = ttk.Button(root, text="New Game", style = 'Large.TButton', command=start_new_game)
new_game_button.pack()

my_gui = Hangman(root)
root.mainloop()