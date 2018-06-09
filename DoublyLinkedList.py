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

    def insertBegining(self,value):
        temp = Node(value)
        if self.head is not None:
            temp.next = self.head
            self.head.prev = temp
            
        self.head = temp        
        
        if self.rear is None:
            self.rear = self.head
            
    def insertEnd(self,value):
        if self.head is None:
            self.insertBegining(value)
        else:
            temp = Node(value)
            curr = self.rear
            curr.next = temp
            temp.prev = curr
            self.rear = temp
            
    
    def insertAfter(self,currValue, newValue):
        if self.head is not None:
            curr = self.head
            keyCapture = False
            temp = Node(newValue)
            while curr.next is not None and keyCapture is False:
                print("Currently Lookig at element " + str(curr.data))
                if curr.data == currValue:
                    keyCapture = True
                    temp.next = curr.next
                    curr.next.prev = temp
                    curr.next = temp
                    temp.prev = curr
                curr = curr.next   
            if keyCapture is False:
                print("Given elment "+ str(currValue) + " does not exist in list. Appending new element at the end of list!")
                self.insertEnd(newValue)                
        else:
            self.insertBegining(newValue)
    
    def insertBefore(self,currValue, newValue):
        if self.head is not None:
            curr = self.rear
            temp =  Node(newValue)
            keyCapture = False
            while curr.prev is not None and keyCapture is False:
                print("checking element " + str(curr.data))
                if curr.data == currValue:
                    keyCapture = True
                    temp.prev = curr.prev
                    curr.prev.next = temp
                    curr.prev = temp
                    temp.next = curr
                curr = curr.prev
            if keyCapture is False:
                print ("Your entered element "+ str(currValue) + " odes not exist in List! Append the element in the begining!")
                self.insertBegining(newValue)
        else:
            insertBegining(newValue)
        
    
    def remove(self,value):
        if self.head is None:
            print ("List is empty!")
        else:
            keyCapture = False
            curr = self.head
            while curr.next is not None and keyCapture == False:
                print("Currently looking at element " + str(curr.data))
                if curr.data == int(value):
                    keyCapture = True
                    #break - Is's not a good programming practiece to use break & continue control construct
                print ("keyCapture = " + str(keyCapture)) 
                #To avoid using break construct
                if keyCapture == False:
                    curr = curr.next
            if keyCapture is False:
                print ("Element " + str(value) + " does not exist!")
            else:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                
    
    
if __name__ == "__main__":
    x = Node(10)
    print(x)
    myList = DLL()
    myList.insertBegining(5)
    myList.insertBegining(4)
    myList.insertBegining(3)
    myList.insertBegining(2)
    myList.insertBegining(1)
    myList.insertBegining(0)
    print ("Executing insertAfter")
    myList.insertAfter(4,10)
    print ("Executing insertAfter")
    myList.insertAfter(9,9)
    print(myList)
    print ("Executing insertBefore")
    myList.insertBefore(4,7)
    print(myList)
    myList.insertAfter(7,0)
    print(myList)
    myList.insertBefore(-1,-1)
    print(myList)
    myList.remove(4)
    print(myList)
