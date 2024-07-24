import random
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import *




# Create a list of words - in seperate file but currently all in one
word_list = [
    "apple", "bread", "crane", "drain", "flame", "grape", "house", 
    "input", "jolly", "knock", "lemon", "melon", "night", "ocean", 
    "piano", "queen", "river", "snake", "toast", "unity", "vocal", 
    "whale", "xenon", "yacht", "zebra"
]

# set for now
random_word = "apple"
user_input = input()

# function chooses a random word from the word_list
# random_word = random.choice(word_list)

#This Wordle_Design class is responsible for updating the design of the Wordle game. It changes the background color of the entry boxes based on the user's guess.
class Wordle_Design:
    # root (tk.Tk): The root window of the Tkinter application.
    # entries (list): A 2D list containing Tkinter Entry widgets representing the Wordle grid.
    def __init__(self, root, entries):
        self.root = root
        self.entries = entries
    #Changes the background color of the specified entry box to green.
    def toGreen(self, row, col):
        #row (int): The row index of the entry box.
        #col (int): The column index of the entry box.
        self.entries[row][col].config(bg='green')

    def toYellow(self, row, col):
        self.entries[row][col].config(bg='yellow')
    
    def toGrey(self, row, col):
        self.entries[row][col].config(bg='grey')

class Word:

    def __init__(self, row_entries, design):
        self.row_entries = row_entries
        self.design = design

    def letter_inword(self):
        for i in self.user_input:
            for j in self.user_input:
                if i==j:
                    return self.design.toYellow(row, i)

    def letter_inindex(self):
        j = 0
        for i in self.user_input:
            if i == random_word[j]:
                self.design.toGreen(row, i)
            else:
                pass
                self.design.toGrey(row, i)
            j+=1
        return self.user_input
    
    global check_word
    def check_word(self, user_input, design):
        print("YAYY")
        if self.user_input == random_word:
            for i in range(5):
                print("YASS")                
                self.design.toGreen(row, i)

# Create a 5x6 grid of entry boxes using Tkinter
    global submit_guess
    def submit_guess(entries):
        global current_row
        # user_word = "".join([entries[current_row][col].get() for col in range(6)])
        if len(row_entries) != 5:
                    print(len(row_entries))
                    messagebox.showerror("Error", "Please enter a 5-letter word.")
                    return None

        if check_word(self, row_entries, "green"):
                    messagebox.showinfo("Congratulations!", "You guessed the word!")
                    print("YYAYYAYYAY")
        else:
                    current_row += 1
                    if current_row >= 6:
                        messagebox.showinfo("Game Over", f"Game over! The word was: {random_word}")
root = tk.Tk()
root = Tk()
# root.geometry("100x100")
root.title("Wordle Game")
entries = []
current_row = 0
for row in range(6):
    row_entries = []
    for col in range(5):
        entry = tk.Entry(root, width=2, font=('Helvetica', 18), justify='center')
        entry.grid(row=row, column=col, padx=5, pady=5)
        def show():
            global name
            name = askstring("Input", "Enter you name")
            for i in name:
                row_entries.append(i)
            entries.append(row_entries)
            print(row_entries)

# B = Button(root, text ="Click", command = show)
# B.place(x=50,y=50)

submit_button = tk.Button(root, text="Submit", command=show)
submit_button = tk.Button(root, text="Submit", command=lambda:[show(),submit_guess(entries)])

submit_button.grid(row=7, columnspan=5)


root.mainloop()

