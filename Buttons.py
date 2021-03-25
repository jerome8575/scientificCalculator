import tkinter as tk
from Display import Display
from EvaluateExpressions import evaluate

class Calculator:

    def __init__(self):
        self.frm_buttons = tk.Frame()

        self.display = Display()

        self.btns = self.createButtons()
        self.placeButtons()

    def createButton(self, text):
        btn = tk.Button(text=text, master=self.frm_buttons)
        btn.config(width=2, height=2)
        btn.bind("<Button-1>", self.buttonPressed)
        return btn

    def createButtons(self):
        buttonOperationText = ["/", "*", "-", "+", ".", "(", ")",
                               "sin", "cos", "tan", "^", "ln", "e^x", "del", "enter"]
        buttons = {}
        # create digits
        for digit in range(10):
            btn = self.createButton(digit)
            buttons[str(digit)] = btn
        for op in buttonOperationText:
            btn = self.createButton(op)
            buttons[op] = btn

        return buttons

    def enter(self):
        expression = self.display.disp["text"]
        result = evaluate(expression)
        self.display.displayAnswer(str(result))

    def deleteEntry(self):
        print("deleting entry")

    def buttonPressed(self, event):
        btn = event.widget
        text = btn["text"]
        if text == "enter":
            self.enter()
        elif text == "del":
            self.deleteEntry()
        else:
            self.display.updateDisplay(str(text))

    def placeButtons(self):

        # place operators
        self.btns["*"].grid(row=1, column=4)
        self.btns["-"].grid(row=2, column=4)
        self.btns["+"].grid(row=3, column=4)

        # place top row trig functions
        self.btns["sin"].grid(row=0, column=1)
        self.btns["cos"].grid(row=0, column=2)
        self.btns["tan"].grid(row=0, column=3)

        # place left column exponential functions
        self.btns["^"].grid(row=0, column=0)
        self.btns["ln"].grid(row=1, column=0)
        self.btns["e^x"].grid(row=2, column=0)
        self.btns["."].grid(row=3, column=0)

        # enter and del button
        self.btns["del"].grid(row=4, column=0)
        self.btns["enter"].grid(row=4, column=4)

        # bottom row
        self.btns["0"].grid(row=4, column=1)
        self.btns["("].grid(row=4, column=2)
        self.btns[")"].grid(row=4, column=3)

        # place digits
        digit = 7
        for i in range(1, 4):
            for j in range(1, 4):
                self.btns[str(digit)].grid(row=i, column=j)
                digit += 1
            digit -= 6

        self.frm_buttons.pack()