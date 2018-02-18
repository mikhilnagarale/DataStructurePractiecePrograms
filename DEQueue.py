#!/usr/bin/python
import numpy as np

class DEQueue:
    front = 0
    rear = 0
    arraySize = 0
    queue = ''

    def __init__(self, queue_size):
        self.arraySize = queue_size
        self.queue = np.empty([queue_size], dtype='int')

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def print_size(self):
        print("Queue size is = " + str(self.rear-self.front))

    def get_front(self):
        return self.queue[self.front]

    def get_rear(self):
        return self.queue[self.rear - 1]

    def insert_at_back(self,element):
        if self.rear == self.arraySize:
            print("Queue Overflow!")
        else:
            self.queue[self.rear] = element
            self.rear = self.rear + 1

    def delete_from_back(self):
        if self.rear == self.front:
            print("Queue Underflow!")
        else:
            self.rear = self.rear - 1
            self.queue[self.rear] = 0

    def insert_at_front(self,element):
        if self.rear == self.arraySize:
            print ("Queue Overflow!")
        else:
            for i in range(self.rear,self.front,-1):
                print ("value of i=" + str(i))
                self.queue[i] = self.queue[i-1]
            self.rear = self.rear + 1
            self.queue[self.front] = element

    def delete_from_front(self):
        if self.rear == self.front:
            print("Queue Underflow!")
        else:
            print("deleting element=" + str(self.queue[self.front]))
            self.queue[self.front] = 0
            self.front = self.front + 1

    def print_queue(self):
        value = ""
        for i in range(self.rear - 1,self.front - 1, -1):
            delimiter = "-->"
            if i == self.front:
                delimiter = ""
            value = value + str(self.queue[i]) + delimiter
        print (value)


def main():
    dq = DEQueue(8)
    dq.delete_from_back()
    dq.delete_from_front()
    dq.print_queue()
    dq.print_size()
    dq.insert_at_back(1)
    dq.insert_at_back(2)
    dq.insert_at_front(8)
    dq.print_queue()
    dq.print_size()
    dq.insert_at_back(3)
    dq.insert_at_back(4)
    dq.insert_at_back(5)
    dq.insert_at_front(7)
    dq.insert_at_front(6)
    dq.print_queue()
    dq.print_size()
    dq.insert_at_back(-1)
    dq.insert_at_front(-2)
    dq.delete_from_front()
    dq.delete_from_front()
    dq.print_queue()
    dq.delete_from_back()
    dq.delete_from_back()
    dq.print_queue()
    dq.print_size()

if __name__ == "__main__":
    main()