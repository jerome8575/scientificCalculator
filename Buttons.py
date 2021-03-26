import tkinter as tk
import tkinter.ttk as ttk
from Display import Display
from EvaluateExpressions import evaluate

class Calculator:

    def __init__(self):
        self.frm_buttons = tk.Frame()

        self.display = Display()

        self.btns = self.createButtons()
        self.placeButtons()

    """def createButtonStyle(self):
        style = ttk.Style()
        style.configure()"""

    def createButton(self, text, color, textColor):
        btn = tk.Button(text=text, master=self.frm_buttons)
        btn.config(width=8, height=4, bg=color, fg=textColor, font="Ubuntu 12")
        btn.bind("<Button-1>", self.buttonPressed)
        return btn

    def createButtons(self):
        operators = ["/", "*", "+", "-", "="]
        functions = ["(", ")", "sin", "cos", "tan", "^", "ln", "e^x", "del"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "(-)"]

        buttons = {}
        # create digits
        for num in numbers:
            btn = self.createButton(num, "#7A7A7A", "White")
            buttons[str(num)] = btn
        for fct in functions:
            btn = self.createButton(fct, "#575757", "White")
            buttons[fct] = btn
        for op in operators:
            btn = self.createButton(op, "#7A7A7A", "White")
            buttons[str(op)] = btn

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
        if text == "=":
            self.enter()
        elif text == "del":
            self.deleteEntry()
        else:
            self.display.updateDisplay(str(text))

    def placeButtons(self):

        # place operators
        self.btns["/"].grid(row=0, column=4)
        self.btns["*"].grid(row=1, column=4)
        self.btns["-"].grid(row=2, column=4)
        self.btns["+"].grid(row=3, column=4)

        # place top row trig functions
        self.btns["sin"].grid(row=0, column=1)
        self.btns["cos"].grid(row=0, column=2)
        self.btns["tan"].grid(row=0, column=3)

        # place left column exponential functions
        self.btns["ln"].grid(row=0, column=0)
        self.btns["^"].grid(row=1, column=0)
        self.btns["("].grid(row=2, column=0)
        self.btns[")"].grid(row=3, column=0)

        # enter and del button
        self.btns["del"].grid(row=4, column=0)
        self.btns["="].grid(row=4, column=4)

        # place digits and ., (-)
        digit = 7
        for i in range(1, 4):
            for j in range(1, 4):
                self.btns[str(digit)].grid(row=i, column=j)
                digit += 1
            digit -= 6
        self.btns["0"].grid(row=4, column=1)
        self.btns["."].grid(row=4, column=2)
        self.btns["(-)"].grid(row=4, column=3)


        self.frm_buttons.pack()