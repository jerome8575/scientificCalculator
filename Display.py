import tkinter as tk

class Display:

    def __init__(self):
        self.frm_display = tk.Frame()
        self.frm_display.pack()

        self.disp = tk.Label(master=self.frm_display)
        self.disp.config(width=10, height=4)
        self.disp.pack()


    def updateDisplay(self, text):
        self.disp.config(text=(self.disp["text"] + text))

    def displayAnswer(self, text):
        self.disp.config(text=text)


