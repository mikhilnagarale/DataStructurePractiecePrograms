class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return '{self.data}'.format(self=self)
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def addElement(self,data):
        '''Creating Temperory Node'''
        tempNode = Node(data)
        
        if self.head == None:
            self.head = tempNode
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = tempNode
            
    def findKey(self,data):
        '''Find Key Element'''
        if self.head == None:
            print('LinkedList is empty')
        else:
            curr = self.head
            while curr.data != data and curr.next != None:
                curr = curr.next
            if curr.data == data:
                return curr
            else:
                return None
            
    def removeElement(self,data):
        '''Find the element & then remove it'''
        prev = self.head
        curr = self.head
        while curr.data != data and curr.next != None:
            prev = curr
            curr = curr.next
            #print('inside loop')
            #print (data,curr.data)
        #Below conditionincludes removal of head element, removl of middle & last element,
        #removal of element in one node list & removal of non existing element. :-)
        if curr.data == data:
            if self.head.data != data:
                prev.next = curr.next
            else:
                self.head = curr.next
        else:
            print ('Element {data} does not exist!'.format(data=data))
        
    def __repr__(self):
        delimiter = '-->'
        curr = self.head
        value=''
        while curr.next != None:
            value = value + str(curr.data) + delimiter
            curr = curr.next
        value = value + str(curr.data)    
        return value
        
if __name__ == "__main__":
    x = Node(10)
    print(x)
    myList = LinkedList()
    myList.addElement(10)
    myList.addElement(20)
    myList.addElement(30)
    myList.addElement(40)
    myList.addElement(50)
    print(myList)
    myList.removeElement(30)
    print(myList)
    myList.removeElement(50)
    print(myList)
    myList.removeElement(10)
    print(myList)
    myList.removeElement(100)
    print(myList)

    
