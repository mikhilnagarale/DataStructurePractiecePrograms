#!/usr/bin/python
#Ref: Logic & Implementation: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheSequentialSearch.html

def sequentialSearch(alist,val):
    pos = 0 
    found =  False
    while pos < len(alist) and not found:
        #print('checking value '+str(alist[pos]))
        if (alist[pos]==val):
            found = True
        else:
            pos = pos + 1
    return found

def orderedSequentialSearch(alist,val):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        #print('checking element '+str(alist[pos]))
        if (alist[pos]==val):
            found = True
        elif alist[pos] > val:
            stop = True
        else:
            pos = pos + 1
    return found        
    
if __name__=="__main__":
    print('Checking element search for non-ordered list')
    myList = [3,9,4,5,346,456,567,56,76,77,876,8,769,78,89,3,24,42,42,4,2342]
    if sequentialSearch(myList,42):
        print('Your search is present in list!')
    print('Checking element search for ordered list')
    myListNew = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]
    if orderedSequentialSearch(myListNew,10):
        print('Your search is present in list!')
    else:
        print('Your search is not present in list!')
    
    
