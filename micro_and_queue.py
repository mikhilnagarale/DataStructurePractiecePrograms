#!/usr/bin/python

'''Micro just purchased a queue and wants to perform N operations on the queue. The operations are of following type:

E x : Enqueue x  in the queue and print the new size of the queue.
D : Dequeue from the queue and print the element that is deleted and the new size of the queue separated by space. If there is no element in the queue then prin − 1 in place of deleted element.

Since Micro is new with queue data structure, he need your help.

Input:
First line consists of a single integer denoting N

Each of the following N lines contain one of the operation as described above.

Output:
For each enqueue operation print the new size of the queue. And for each dequeue operation print two integers, deleted element (−1, if queue is empty) and the new size of the queue.

Constraints:
1≤N≤100
1≤x≤100'''
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

'''
SAMPLE INPUT - SAMPLE OUTPUT
5               
E 2             1 
D               2 0
D               -1 0
E 3             1
D               3 0
'''

# Write your code here
import numpy as np

val = input ()
front = 0
rear = 0
q = np.empty ([int (val)], dtype='int')


def get_size():
    return rear - front


def is_empty():
    if front == rear:
        return True
    else:
        return False


def get_rear():
    if is_empty ():
        return -1
    else:
        return q[rear - 1]


def get_front():
    if is_empty ():
        return -1
    else:
        return q[front]


for i in range (0, int (val)):
    value = input ()
    output = ''
    if len (value) == 1:
        if value == 'D':
            output = output + str (get_front ()) + " "
            if not (is_empty ()):
                front = front + 1
    else:
        X, Y = value.split (" ")
        if X == 'E':
            q[rear] = int (Y)
            rear = rear + 1

    output = output + str (get_size ())
    print(output)


