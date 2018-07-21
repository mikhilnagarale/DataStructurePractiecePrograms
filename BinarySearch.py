#!/usr/bin/python
#Ref: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheBinarySearch.html

def binarySearch(alist,item):
    first = 0
    last = len(alist)-1
    found = False
    while not found and first <=last:
        mid = (first+last)//2
        print ('mid index='+str(mid)+' element at mid='+str(alist[mid])+' firstIndex='+str(first)+' lastIndex='+str(last))
        if alist[mid] == item:
            found = True
        else:
            if item < alist[mid]:
                last = mid -1
            else:
                first = mid + 1
    return found

def recBinarySearch(alist,item):
    print(alist)
    found = False
    mid = (len(alist)-1)//2
    #print('mid='+str(mid))
    #print('length of list = '+str(len(alist)))
    #print(0)
    while len(alist) > 0 and not found:
        #print(1)
        print('found='+str(found))
        print('mid element='+str(alist[mid]))
        print('alist[mid]='+str(alist[mid])+' item='+str(item))
        if alist[mid] == item:
            return True
        else:
            #print(2)
            if item < alist[mid]:
                return recBinarySearch(alist[:mid-1],item)
            else:
                #print(3)
                return recBinarySearch(alist[mid+1:],item)
    return  False     
    

    
    

if __name__=="__main__":
    myList = [1,2,3,4,5,6,7,8,9,11,15,17,19,20,25,27]
    print(myList)
    print('Binary Search non-recursive way!')
    if binarySearch(myList,16):
        print ('Element Found!')
    else:
        print ('Element Not Found!')
        
    print('Binary Search recursive way!')    
    if recBinarySearch(myList,16):
        print ('Element Found!')
    else:
        print ('Element Not Found!')
    print('Binary Search recursive way!')            
    if recBinarySearch(myList,17):
        print ('Element Found!')
    else:
        print ('Element Not Found!')
        
   
                    
            
