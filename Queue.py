#!/usr/bin/python
import numpy as np


class Queue:
    arraySize = 0
    queue = ''
    front = 0
    rear = 0

    def __init__(self, queue_size):
        self.arraySize = queue_size
        self.queue = np.empty([queue_size], dtype='int')

    def is_empty(self):
        if self.rear == self.front:
            return True
        else:
            return False

    def en_queue(self, val):
        if self.rear < self.arraySize:
            self.queue[self.rear] = val
            self.rear = self.rear + 1
        else:
            print("Overflow!")

    def de_queue(self):
        if self.is_empty():
            print("Underflow!")
        else:
            print(str(self.queue[self.front]))
            self.front = self.front + 1

    def print_queue(self):
        value = ''
        for i in range(self.front,self.rear):
            value = value + str(self.queue[i]) + "\t"
        print (value)


    def get_front(self):
        return self.front

    def get_rear(self):
        return self.rear

    def get_size(self):
        return self.rear - self.front


def main():
    q = Queue(7)
    q.get_front()
    q.de_queue()
    q.en_queue(7)
    q.en_queue(6)
    q.en_queue(5)
    q.en_queue(4)
    q.get_front()
    q.get_rear()
    q.de_queue()
    q.de_queue()
    q.de_queue()
    q.de_queue()
    q.de_queue()
    q.en_queue(3)
    q.en_queue(2)
    q.en_queue(1)
    q.en_queue(0)
    q.de_queue()
    q.de_queue()
    q.de_queue()
    q.de_queue()
    q.en_queue(0)

if __name__ == "__main__":
    main()





