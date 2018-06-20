#!/usr/bin/python
#Ref: https://cs.stackexchange.com/questions/41719/the-most-appropriate-way-to-implement-a-heap-is-with-an-array-rather-than-a-link
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
#Why Binary Search Tree is not stored in array-
#Binary search tree is use for fastr searching & storing the elements in sorted order. 
#If we store the BST in arry then it won't be able to store the elements in sorted order using same logic as childerns: 2K,2K+1.
#There will be additional overhead to store the elements ingiven specific order.
#The reason for storing the Heap (min/max) in array is that array indexes will natuaraly act as priority maintanance & we don't need to keep prority explicitly.
#Only thing we need to consider is every parent should be either greater than (max heap) child or less than (min heap) child.
#Hence different datastructure are used to store heap(array) and BST(pointer based nodes) .
