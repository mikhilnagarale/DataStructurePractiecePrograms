#!/usr/bin/python
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

if __name__=="__main__":
    myList = [1,2,3,4,5,6,7,8,9,11,15,17,19,20,25,27]
    print(myList)
    if binarySearch(myList,16):
        print ('Element Found!')
    else:
        print ('Element Not Found!')
        
                
            
