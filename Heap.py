#!/usr/bin/python
#Question- Why Heap is stored in arry . Why Linked list or any other data structure like pointer based nodes used to store Heap?
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
