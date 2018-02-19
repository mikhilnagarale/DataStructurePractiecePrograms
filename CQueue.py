#!/usr/bin/python
import numpy as np

class CQueue:
    arraySize = 0
    front = 0
    rear = 0
    queue = ''
    count = 0
    def __init__(self,sizeOfQueue):
        self.arraySize = sizeOfQueue
        self.queue = np.empty([self.arraySize], dtype='int')

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def get_size(self):
        return self.count

    def print_front(self):
        print ("element at front="+str(self.queue[self.front]))

    def print_rear(self):
        print ("element at rear="+str(self.queue[self.rear - 1]))

    def en_queue(self, element):
        if self.count == self.arraySize:
            print ("Queue Overflow!")
        else:
            self.queue[self.rear] = element
            self.rear = (self.rear + 1)%self.arraySize
            self.count = self.count + 1

    def de_queue(self):
        if self.count == 0:
            print("Queue Underflow!")
        else:
            self.queue[self.front] = 0
            self.front = (self.front + 1) % self.arraySize
            self.count = self.count - 1

    def print_queue(self):
        value = ""
        current_index = self.rear - 1
        delimiter = "-->"

        for i in range(0,self.count):
            if i == (self.count -1):
                delimiter = ""

            index = ((current_index - i) + self.arraySize) % self.arraySize
            value = value + str(self.queue[index]) + delimiter

        print (value)

def main():
    q = CQueue(6)
    print(str(q.is_empty()))
    print(str(q.get_size()))
    q.de_queue()
    q.en_queue(6)
    q.en_queue(5)
    q.en_queue(4)
    q.print_queue()
    q.print_front()
    q.print_rear()
    q.en_queue(3)
    q.en_queue(2)
    q.en_queue(1)
    q.en_queue(0)
    q.print_queue()
    q.print_front()
    q.print_rear()
    q.de_queue()
    q.de_queue()
    q.en_queue(9)
    q.print_queue()
    q.en_queue(10)
    q.print_queue()
    q.print_front()
    q.print_rear()


if __name__ == "__main__":
    main()
