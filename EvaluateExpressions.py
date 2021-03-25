from StackAndQueue import Stack, Queue
import operator
import math

def parse(expression):
    expressionList = []
    expressionList[:0] = expression
    expressionList.insert(0, "(")
    expressionList.append(")")
    exp = []
    functions = ["sin", "cos", "tan", "ln"]
    operators = ["+", "-", "*", "/", "^"]
    fct = ""
    num = ""
    numFilled = False
    for char in expressionList:
        if char.isnumeric():
            num+=char
            numFilled = True
        else:
            if numFilled == True:
                exp.append(num)
                num = ""
                numFilled = False

            if char == "(" or char == ")":
                exp.append(char)
            elif char.isalpha():
                fct += char
                if fct in functions:
                    exp.append(fct)
                    fct = ""
            elif char in operators:
                exp.append(char)

    return exp

def convertToRPN(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    functions = ["sin", "cos", "tan", "ln"]
    exp = parse(expression)
    operators = Stack()
    output = Queue()

    for elem in exp:
        if elem.isnumeric():
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
                    break
                if topStack in functions:
                    continue
                elif precedence[elem] <= precedence[topStack]:
                    output.push(operators.pop())
            operators.push(elem)

    while not operators.isEmpty():
        output.push(operators.pop())
    return output.returnQueueAsList()

def evaluatePostix(pfExpression):
    ops = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul, "^": math.pow}
    functions = {"sin": math.sin, "cos": math.cos, "tan": math.tan, "ln": math.log}
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
            stack.push(elem)

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

def testconvertToRPN():
    print(convertToRPN("sin(3)"))
    print(convertToRPN("5+44"))
    print(convertToRPN("sin(3)"))
    print(convertToRPN("sin(cos(sin(45+ln(2))))"))

def testEvaluate():
    print(evaluate("sin(3)"))
    print(evaluate("sin(cos(sin(45+ln(2))))"))
