#/usr/bin/python
class Node:
    def __init__(self,value):
        self.next = None
        self.prev = None
        self.data = value
    def __repr__(self):
        return '{self.data}'.format(self=self)
##Just using Abbrivation ;-) Obviously any one can predict it's Doubly Linked List (DLL)
#It's a good way to hide everything by giving everything which is mostly used in Companies by so called Good Employees :) Though I don't like it :)
class DLL:
    def __init__(self):
        self.head = None
        self.rear = None
    
    def __repr__(self):
        delim = '->'
        display = ''
        #This is the best thing I like to type in python. No need to explain :-)
        if self.head is not None and self.rear is not None:
            curr = self.head
            if curr.next is None:
                delim = ''
                display = str(curr) + delim
            while curr.next is not None:
                display = display + str(curr) + delim
                curr = curr.next
            display = display + str(curr)    
        return display
    
    #def insertAfter(self,currValue, newValue):
    #def insertBefore(self,currValue, newValue):
    def insertBegining(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
        if self.rear is None:
            self.rear = self.head
            
    #def insertEnd(self,value):
    #def remove(self,value):
    
    
if __name__ == "__main__":
    x = Node(10)
    print(x)
    myList = DLL()
    myList.insertBegining(5)
    myList.insertBegining(4)
    myList.insertBegining(3)
    print(myList)
