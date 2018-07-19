#!/usr/bin/python
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

if __name__=="__main__":
    myList = [3,9,4,5,346,456,567,56,76,77,876,8,769,78,89,3,24,42,42,4,2342]
    if sequentialSearch(myList,42):
        print('Your search is present in list!')
