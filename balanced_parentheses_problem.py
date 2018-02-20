#!/usr/bin/python
import numpy as np

queue = ''
top = -1


def check(value, size):
    global queue
    global top
    queue = np.empty([size], dtype='string')
    for element in value:
        if element == '(':
            top = top + 1
            queue[top] = element
        if element == ')':
            top = top - 1

    if top == -1:
        print("String is balanced!")
    else:
        print("String is unbalanced!")


def main():
    a = np.array(['(', 'a', '+', '(', 'b', '+', 'c', ')', ')'])
    b = np.array(['(', 'a', '+', '(', 'b', '+', 'c', ')'])
    check(a, 9)
    check(b, 9)


if __name__ == "__main__":
    main()
