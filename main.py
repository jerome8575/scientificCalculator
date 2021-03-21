import tkinter as tk
from EvaluateExpressions import evaluate

window = tk.Tk()

frm_buttons = tk.Frame()
frm_display = tk.Frame()

def enter():
    expression = disp["text"]
    result = evaluate(expression)
    displayAnswer(str(result))
def deleteEntry():
    print("deleting entry")
def updateDisplay(text):
    disp.config(text=(disp["text"]+text))

def displayAnswer(text):
    disp.config(text=text)

def buttonPressed(event):
    btn = event.widget
    text = btn["text"]
    if text == "enter":
        enter()
    elif text == "del":
        deleteEntry()
    else:
        updateDisplay(str(text))

def createButton(text):
    btn = tk.Button(text=text, master=frm_buttons)
    btn.config(width=2, height=2)
    btn.bind("<Button-1>", buttonPressed)
    return btn


def createButtons():
    buttonOperationText = ["/", "*", "-", "+", ".", "(", ")",
                           "sin", "cos", "tan", "^", "ln", "e^x", "del", "enter"]
    buttons = {}
    # create digits
    for digit in range(10):
        btn = createButton(digit)
        buttons[str(digit)] = btn
    for op in buttonOperationText:
        btn = createButton(op)
        buttons[op] = btn

    return buttons


def placeButtons(btns):

    # place operators
    btns["/"].grid(row=0, column=4)
    btns["*"].grid(row=1, column=4)
    btns["-"].grid(row=2, column=4)
    btns["+"].grid(row=3, column=4)

    # place top row trig functions
    btns["sin"].grid(row=0, column=1)
    btns["cos"].grid(row=0, column=2)
    btns["tan"].grid(row=0, column=3)

    # place left column exponential functions
    btns["^"].grid(row=0, column=0)
    btns["ln"].grid(row=1, column=0)
    btns["e^x"].grid(row=2, column=0)
    btns["."].grid(row=3, column=0)

    # enter and del button
    btns["del"].grid(row=4, column=0)
    btns["enter"].grid(row=4, column=4)

    # bottom row
    btns["0"].grid(row=4, column=1)
    btns["("].grid(row=4, column=2)
    btns[")"].grid(row=4, column=3)


    # place digits
    digit = 7
    for i in range(1, 4):
        for j in range(1, 4):
            btns[str(digit)].grid(row=i, column=j)
            digit+=1
        digit-=6

def createDisplayScreen():

    display = tk.Label(master=frm_display)
    display.config(width=10, height=4)
    return display

def placeDisplay():
    display = createDisplayScreen()
    display.pack()
    return display


placeButtons(createButtons())
disp = placeDisplay()

frm_display.pack()
frm_buttons.pack()

window.mainloop()