import tkinter as tk

class Display:

    def __init__(self):
        self.frm_display = tk.Frame()
        self.frm_display.pack(pady=5)

        self.disp = tk.Label(master=self.frm_display, bg="light gray", font="Ubuntu 11")
        self.disp.config(width=13, height=3)
        self.disp.pack()


    def updateDisplay(self, text):
        self.disp.config(text=(self.disp["text"] + text))

    def displayAnswer(self, text):
        self.disp.config(text=text)


