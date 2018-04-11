#!/usr/bin/python

'''
Find first character in given word which is repeating. 
Eg- 
amazon - a
paranormal - a
pizza - z
'''
import sys
word=sys.argv[1]
my_dict={}
for c in word:
    if c in my_dict.keys():
        my_dict[c] = my_dict[c] + 1
    else:
        my_dict[c] = 1

for c in word:
    if my_dict.get(c) > 1:
        print ('First repeating character is = ' + c)
        break


 



