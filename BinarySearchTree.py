class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
        
    def insert(self,data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
     
    def findval(self,val):
        if val < self.data:
            if self.left is None:
                print ('value '+str(val)+' is not found')
            else:
                self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                print ('value '+str(val)+' is not found')
            else:
                self.right.findval(val)
        else:
            print ('value '+str(val)+' is found')
        
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(str(self.data))
        if self.right:
            self.right.PrintTree()    
    
root = Node(14)
root.insert(8)
root.insert(12)
root.insert(11)
root.insert(13)
root.insert(6)
root.insert(9)
root.PrintTree()
root.findval(11)
root.findval(10)
