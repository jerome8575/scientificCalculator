import tkinter as tk

class Display:

    def __init__(self):
        self.frm_display = tk.Frame()
        self.frm_display.pack(pady=5)

        self.disp = tk.Label(master=self.frm_display, bg="#343434", fg="White", font="Ubuntu 32", anchor='e')
        self.disp.config(width=16, height=3)
        self.disp.pack()


    def updateDisplay(self, text):
        self.disp.config(text=(self.disp["text"] + text))

    def displayAnswer(self, text):
        self.disp.config(text=text)


