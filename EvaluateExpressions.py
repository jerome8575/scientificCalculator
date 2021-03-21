from StackAndQueue import Stack, Queue
import operator

def parse(expression):
    exp = []
    functions = ["sin", "cos", "tan", "ln"]
    fct = ""
    for char in expression:
        if char.isalpha():
            fct+=char
            if fct in functions:
                exp.append(fct)
                fct = ""
        else:
            exp.append(char)
    return exp

def convertToRPN(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
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
        else:
            while not operators.isEmpty():
                topStack = operators.peep()
                if topStack == "(":
                    break
                elif precedence[elem] <= precedence[topStack]:
                    output.push(operators.pop())
            operators.push(elem)

    while not operators.isEmpty():
        output.push(operators.pop())
    return output.returnQueueAsList()

def evaluatePostix(pfExpression):
    ops = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}
    stack = Stack()
    for i in range(len(pfExpression)):
        elem = pfExpression[i]
        if elem not in ops.keys():
            stack.push(elem)
        else:
            a = float(stack.pop())
            b = float(stack.pop())
            r = ops[elem](b,a)
            stack.push(r)
    result = stack.pop()
    return result


def evaluate(expression):
    print("evaluating")
    pf = convertToRPN(expression)
    return evaluatePostix(pf)




