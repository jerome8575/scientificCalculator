import tkinter as tk
from Buttons import Calculator

# create tkinter window and set background to black
window = tk.Tk()
window.configure(bg="Black")

# create calculator object which creates and places the widgets
calc = Calculator()

# window loop to run program
window.mainloop()
