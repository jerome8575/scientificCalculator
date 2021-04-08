import tkinter as tk
from Display import Display
from EvaluateExpressions import evaluate
import math


# calculator creates buttons and places them, contains functions to handle button clicks
# and creates a display object which is the screen of our calculator
class Calculator:

    def __init__(self):
        self.frm_buttons = tk.Frame()

        self.display = Display()

        self.btns = self.createButtons()
        self.placeButtons()



    def createButton(self, text, color, textColor):
        btn = tk.Button(text=text, master=self.frm_buttons)
        btn.config(width=8, height=4, bg=color, fg=textColor, font="Ubuntu 12")
        btn.bind("<Button-1>", self.buttonPressed)
        return btn

    def createButtons(self):

        """ creates buttons with specified color, and text, appends them to a dictionary and returns the dictionary"""

        operators = ["/", "*", "+", "-", "="]
        functions = ["(", ")", "sin", "cos", "tan", "^", "\u221A" ,"ln", "\u2190", "clear", "\u03C0", "e", "x^2"]
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
        updatedText = ""
        if not self.display.history.isEmpty():
            self.display.history.pop()
            if not self.display.history.isEmpty():
                updatedText = self.display.history.peep()

        self.display.displayAnswer(updatedText)

    def clearScreen(self):
        self.display.history.clearStack()
        self.display.displayAnswer("")

    def buttonPressed(self, event):

        functions = ["sin", "cos", "tan", "ln", "\u221A"]

        btn = event.widget
        text = btn["text"]

        if text in functions:
            text+="("
        elif text == "x^2":
            text = "^2"

        if text == "=":
            self.enter()
        elif text == "\u2190":
            self.deleteEntry()
        elif text == "clear":
            self.clearScreen()
        else:
            self.display.updateDisplay(str(text))

    def placeButtons(self):

        """ using the btns dictionary created earlier, places all the buttons on the window"""
        # first row exponentials
        self.btns["\u221A"].grid(row=0, column=0)
        self.btns["^"].grid(row=0, column=1)
        self.btns["ln"].grid(row=0, column=2)
        self.btns["x^2"].grid(row=1, column=0)

        # place operators
        self.btns["/"].grid(row=1, column=4)
        self.btns["*"].grid(row=2, column=4)
        self.btns["-"].grid(row=3, column=4)
        self.btns["+"].grid(row=4, column=4)

        # place top row trig functions
        self.btns["sin"].grid(row=1, column=1)
        self.btns["cos"].grid(row=1, column=2)
        self.btns["tan"].grid(row=1, column=3)

        # top row parentheses
        self.btns["("].grid(row=0, column=3)
        self.btns[")"].grid(row=0, column=4)

        # commands
        self.btns["\u2190"].grid(row=5, column=0)
        self.btns["clear"].grid(row=4, column=0)
        self.btns["="].grid(row=5, column=4)

        # constants pi and e
        self.btns["\u03C0"].grid(row=3, column=0)
        self.btns["e"].grid(row=2, column=0)

        # place digits and ., (-)
        digit = 7
        for i in range(1, 4):
            for j in range(1, 4):
                self.btns[str(digit)].grid(row=i+1, column=j)
                digit += 1
            digit -= 6
        self.btns["0"].grid(row=5, column=1)
        self.btns["."].grid(row=5, column=2)
        self.btns["(-)"].grid(row=5, column=3)


        self.frm_buttons.pack()