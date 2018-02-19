#!/usr/bin/python
import numpy as np

class Stack:
    top = -1
    arraySize = 0
    stack = ''

    def __init__(self, size):
        self.stack = np.empty([size], dtype='str')
        self.arraySize = size

    def get_size(self):
        return self.top + 1

    def is_full(self):
        if self.top == self.arraySize - 1:
            return True
        else:
            return False

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def get_top(self):
        return self.stack[self.top]

    def push(self, element):
        if self.is_full():
            print("Stack Overflow!")
        else:
            self.top = self.top + 1
            self.stack[self.top] = element

    def pop(self):
        if self.is_empty():
            print ("stack Empty!")
        else:
            print (self.stack[self.top])
            self.top = self.top - 1

    def print_stack(self):
        output = ''
        delimiter = '|-->'
        for i in range(0, self.top + 1):
            if i == self.top:
                delimiter = ''
            output = output + self.stack[i] + delimiter
        print(output)


def main():
    s = Stack(5)
    s.pop()
    s.push('a')
    s.push('b')
    s.push('c')
    s.push('d')
    s.push('e')
    s.push('f')
    s.print_stack()
    s.pop()
    s.pop()
    s.print_stack()
    s.push('x')
    s.print_stack()
    s.push('y')
    s.print_stack()




if __name__ == "__main__":
    main()