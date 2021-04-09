from StackAndQueue import Stack, Queue
import operator
import math

def isUnaryNegative(index, exp):
    operators = ["+", "-", "*", "/", "^"]
    if exp[index - 1] == "(" or exp[index] in operators:
        return True
    return False

def parse(expression):

    print(expression)
    expressionList = list(expression)
    expressionList.insert(0, "(")
    expressionList.append(")")
    exp = []

    functions = ["sin", "cos", "tan", "ln"]
    operators = ["+", "\u2013", "*", "/", "^"]
    pi = "π"
    sqrt = "√"


    fct = ""
    num = ""
    numFilled = False
    index = 0
    for char in expressionList:
        if char.isdecimal() or char == ".":
            num += char
            numFilled = True
        else:
            if numFilled == True:
                exp.append(num)
                num = ""
                numFilled = False
            if char == "(" or char == ")":
                exp.append(char)
            elif char == pi:
                exp.append(math.pi)
            elif char == "e":
                exp.append(math.exp(1))
            elif char == sqrt:
                exp.append("sqrt")
            elif char.isalpha():
                fct += char
                if fct in functions:
                    exp.append(fct)
                    fct = ""
            elif char == "-":
                exp.append("$")
            elif char in operators:
                exp.append(char)
        index+=1
    return exp

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def convertToRPN(expression):
    precedence = {"+": 2, "\u2013": 2, "*": 3, "/": 3, "^": 4, "sqrt": 4, "sin": 1, "cos": 1, "tan": 1, "ln": 1, "$":5}
    functions = ["sin", "cos", "tan", "ln", "$"]
    exp = parse(expression)
    operators = Stack()
    output = Queue()

    for elem in exp:
        if isfloat(elem) or elem.isdecimal():
            print(elem)
            output.push(elem)
        elif elem == "(":
            operators.push(elem)
        elif elem == ")":
            while not operators.isEmpty():
                topStack = operators.peep()
                if topStack == "(":
                    operators.pop()
                    break
                else:
                    output.push(operators.pop())
        elif elem in functions:
            operators.push(elem)
        else:
            while not operators.isEmpty():
                topStack = operators.peep()
                if topStack == "(":
                    operators.pop()
                elif precedence[elem] <= precedence[topStack]:
                    output.push(operators.pop())
                else:
                    break
            operators.push(elem)

    while not operators.isEmpty():
        output.push(operators.pop())
    return output.returnQueueAsList()

def unaryNegative(num):
    return num * (-1)

def evaluatePostix(pfExpression):
    ops = {"+": operator.add, "\u2013": operator.sub, "/": operator.truediv, "*": operator.mul, "^": math.pow}
    functions = {"sin": math.sin, "cos": math.cos, "tan": math.tan, "ln": math.log, "sqrt": math.sqrt, "$": unaryNegative}
    stack = Stack()
    for i in range(len(pfExpression)):
        elem = pfExpression[i]
        if elem in functions.keys():
            num = float(stack.pop())
            stack.push(functions[elem](num))
        elif elem in ops.keys():
            a = float(stack.pop())
            b = float(stack.pop())
            r = ops[elem](b, a)
            stack.push(r)
        else:
            stack.push(float(elem))

    result = stack.pop()
    return round(result, 10)


def evaluate(expression):
    print("evaluating")
    pf = convertToRPN(expression)
    return evaluatePostix(pf)


def testParse():
    print(parse("sin(56)"))
    print(parse("5^41"))
    print(parse("34+23"))
    print(parse("-6 + 3"))
    print(parse("2.3*6"))

def testconvertToRPN():
    print(convertToRPN("sin(3)"))
    print(convertToRPN("5+44"))
    print(convertToRPN("sin(cos(sin(45+ln(2))))"))
    print(convertToRPN("-6 + 3"))
    print(convertToRPN("sin(sin(2+3))"))
    print("2.3*6")

def testEvaluate():
    print(evaluate("sin(3)"))
    print(evaluate("sin(cos(sin(45+ln(2))))"))
    print(evaluate("-6"))

