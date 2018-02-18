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

    def get_size(self):
        return self.rear-self.front

    def get_front(self):
        return self.queue[self.front]

    def get_rear(self):
        return self.queue[self.rear]

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
            self.rear = self.rear + 1
            self.queue[self.rear] = 0

    def insert_at_front(self,element):
        if self.rear == self.arraySize:
            print ("Queue Overflow!")
        else:
            self.rear = self.rear + 1
            for i in range(self.rear,self.front,-1):
                self.queue[i] = self.queue[i-1]
            self.queue[self.front] = element

    def delete_from_front(self):
        if self.rear == self.front:
            print("Queue Underflow!")
        else:
            print("deleting element=" + str(self.queue[self.self.front]))
            self.queue[self.front] = 0
            self.front = self.front + 1


