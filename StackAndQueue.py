class Stack:
    stack = []

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        elem = self.stack[-1]
        del self.stack[-1]
        return elem

    def peep(self):
        return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
    def printStack(self):
        print(self.stack)


class Queue:
    queue = []

    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        elem = self.queue[0]
        del self.queue[0]
        return elem

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
    def printQueue(self):
        print(self.queue)

    def returnQueueAsList(self):
        return self.queue