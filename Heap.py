#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ref - Why different data structure?: https://cs.stackexchange.com/questions/41719/the-most-appropriate-way-to-implement-a-heap-is-with-an-array-rather-than-a-link
#Ref - How to implement Heap : http://interactivepython.org/courselib/static/pythonds/Trees/BinaryHeapImplementation.html
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question- Why Heap is stored in arry . Why Linked list or any other data structure like pointer based nodes used to store Heap?
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#Why Binary search tree is not stored in Array since heap & binary search tree both are trees?
#ANS-
#It doesn't make any sense at all to implement a heap as a linked list. Heaps are inherently binary trees. 
#You can store a heap in an array because it's easy to compute the array index of a node's children: 
#the children of the node at position K live at positions 2K and 2K+1. 
#It's massively more efficient to find the Kth element of an array than the Kth element of a linked list.
#
#Advantages of storing a heap as an array rather than a pointer-based binary tree include the following.
#
#Lower memory usage (no need to store three pointers for every element of the heap).
#Easier memory management (just one object allocated, rather than N).
#Better locality of reference (the items in the heap are relatively close together in memory rather than scattered wherever the allocator put them).
#Why Binary Search Tree is not stored in array-
#Binary search tree is use for fastr searching & storing the elements in sorted order. 
#If we store the BST in arry then it won't be able to store the elements in sorted order using same logic as childerns: 2K,2K+1.
#There will be additional overhead to store the elements ingiven specific order.
#The reason for storing the Heap (min/max) in array is that array indexes will natuaraly act as priority maintanance & we don't need to keep prority explicitly.
#Only thing we need to consider is every parent should be either greater than (max heap) child or less than (min heap) child.
#Hence different datastructure are used to store heap(array) and BST(pointer based nodes) .
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
class Heap:
    def __init__(self,heapType):
        self.heapList = [0]
        self.heapsize = 0
        self.heapType = heapType
        
    def __repr__(self):
        return str(self.heapList)
    
    #In this method we compare child element with it's parent and push child to higher/up level based on heapType
    def pushUp(self,index):
        while index // 2 > 0:
            #Comparing newly added leaf element with it's parent node
            if self.heapList[index//2] > self.heapList[index] and self.heapType == 'min':
                temp = self.heapList[index//2]
                self.heapList[index//2] = self.heapList[index]
                self.heapList[index] = temp
            if self.heapList[index//2] < self.heapList[index] and self.heapType == 'max':
                temp = self.heapList[index//2]
                self.heapList[index//2] = self.heapList[index]
                self.heapList[index] = temp    
            index = index//2
            
    #This method will return appropriate index of child element based on heapType
    def getChild(self,index):
        if self.heapsize == 2*index:
            print('heapsize='+str(self.heapsize)+' mc='+str(2*index))
            return 2*index
        else:
            if self.heapType == 'min':
                if self.heapList[2*index] < self.heapList[2*index+1]:
                    return 2*index
                else:
                    return 2*index+1
            else:
                if self.heapList[2*index] > self.heapList[2*index+1]:
                    return 2*index
                else:
                    return 2*index+1
                
    #In this method we compare Parent with it's child elements and push Parent down by comparing between it's child based on heapType.
    def pushDown(self,index):
        while self.heapsize >= 2*index:
            mc = self.getChild(index)
            if self.heapList[index] > self.heapList[mc] and self.heapType == 'min':
                temp = self.heapList[mc]
                self.heapList[mc] = self.heapList[index]
                self.heapList[index] = temp
                print(str(self.heapList))
            if self.heapList[index] < self.heapList[mc] and self.heapType == 'max':
                temp = self.heapList[mc]
                self.heapList[mc] = self.heapList[index]
                self.heapList[index] = temp
                print(str(self.heapList))                
            index = mc
            print ('heapsize='+str(self.heapsize)+' index='+str(index))
            
        
        
        
    def delete(self):
        print("Deleting the Top element")
        print(str(self.heapList))
        temp = self.heapList[1]
        self.heapList[1] = self.heapList[self.heapsize]
        print(str(self.heapList))
        self.heapList.pop()
        self.heapsize = self.heapsize - 1
        self.pushDown(1)
        
    def buildHeap(self,sampleList,heapType):
        index = len(sampleList)//2
        self.heapsize = len(sampleList)
        self.heapList = [0]+sampleList
        self.heapType = heapType
        while index > 0:
            print ('index='+str(index))
            self.pushDown(index)
            index = index - 1
        
    
    def insert(self,val):
        self.heapList.append(val)
        self.heapsize = self.heapsize + 1
        self.pushUp(self.heapsize)

if __name__=="__main__":
    print('-->Testing min heap'+"\n")
    myHeap = Heap('min')        
    print (myHeap)
    myHeap.insert(20)
    myHeap.insert(10)
    myHeap.insert(15)
    myHeap.insert(13)
    myHeap.insert(9)
    print (myHeap)
    myHeap.insert(25)
    myHeap.insert(17)
    myHeap.insert(4)
    print(myHeap)
    print("\n"+'-->Testing Element deletion in min heap'+"\n")
    myHeap.delete()
    print(myHeap)
    print("\n"+'-->Testing max heap'+"\n")
    myHeap = Heap('max')        
    print (myHeap)
    myHeap.insert(20)
    myHeap.insert(10)
    myHeap.insert(15)
    myHeap.insert(13)
    myHeap.insert(9)
    print (myHeap)
    myHeap.insert(25)
    myHeap.insert(17)
    myHeap.insert(4)
    print(myHeap)
    myList = [9, 5, 6, 2, 3]
    print("\n"+'-->Testing Element deletion in max heap'+"\n")
    myHeap.delete()
    print(myHeap)
    print("\n"+'-->Testing the building of min heap'+"\n")
    myHeap.buildHeap(myList,'min')
    print(myHeap)
    print("\n"+'-->Testing the building of max heap'+"\n")
    myHeap.buildHeap(myList,'max')
    print(myHeap)

    
