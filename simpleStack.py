class SimpleStack():
    def __init__(self):
        self.stack = []

    def push_back(self, value):
        '''Push an element to the end of the stack'''
        self.stack.append(value)

    def pop(self):
        '''Pop the top element of the stack'''
        self.stack.pop()

    def peek(self):
        '''Visit the top element of the stack'''
        return self.stack[-1] if len(self.stack) > 0 else None

    def print_stack(self):
        '''Print the stack's element'''
        print(self.stack)