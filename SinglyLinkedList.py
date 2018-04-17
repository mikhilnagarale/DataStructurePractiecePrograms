class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return '{self.data}'.format(self=self)


class LinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self,data):
        '''Add element at the begining of Linked List'''
        tempNode = Node(data)
        tempNode.next =self.head
        self.head = tempNode
        
        
    def addNode(self,data):
        '''Insert element at the end of list'''
        tempNode = Node(data)
        curr = self.head
        if self.head is None:
            self.head = tempNode
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = tempNode
            
    def __repr__(self):
        connector = '-->'
        value=''
        curr = self.head
        if self.head is not None:
            while curr.next is not None:
                value = value + str(curr.data) + connector
                curr = curr.next
            value = value + str(curr.data)
            return value
        else:
            return ''
    
    def findKey(self,data):
        '''Finding the key in an LinkedList takes O(n) time'''
        curr = self.head
        '''
        Below condition is implemented as 
        
        while curr and curr.data != data: 
        
        in solution provided by Dan Bader (Ref: https://dbader.org/blog/python-linked-list).
        It's Giving same result but I'm unable to understand how it does?
        If anyone gets it please let me know 
        Thanks in Advance!
        '''
        while  curr != None and curr.data != data: 
            curr = curr.next
        return curr
    
    def remove(self,data):
        '''Removing the element'''
        curr = self.head
        prev = None
        while curr != None and curr.data != data:
            prev = curr
            curr = curr.next
        
        if curr == None:
            print('Element is not present')
        else:
            prev.next = curr.next
            curr = None
            
    
            
if __name__ == "__main__":
    my_list = LinkedList()
    my_list
    my_list.addNode(10)
    my_list.addNode(9)
    my_list.addNode(8)
    my_list.addNode(7)
    my_list.prepend(0)
    print(my_list)
    myNode = my_list.findKey(10)
    print(myNode)
    myNode2 = my_list.findKey(4)
    print(myNode2)
    print(my_list)
    my_list.remove(9)                
    print(my_list)
    
    
    
    
