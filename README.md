# Data Structures

![PyPI](https://img.shields.io/badge/python-3.4--3.6-5ba7e5.svg)
![PyPI](https://img.shields.io/badge/scripts-3-72b73a.svg)


## Implementing data structures and algorithms in Python


### Linked List
##### LinkedList.py 
##### CircularLinkedList.py <br>
A linked list is a linear collection of data elements, in which each element has a pointer that points to the next element. This data structure is composed of nodes, each of which conists of data and a link to the next node in sequence. Applications of this data structure include higher efficiency (greater than for arrays) of insertion and deletion of data elements and links at any position. A circular linked list can either be a singly or doubly linked list in which the tail node points to the head node and thus contains no null pointers. Disadvantages of a linked list are that they have worse cache locality and they have a higher space comlexity than arrays due to the memory storage used by the pointers. Another disadvantage is that a linked list's nodes must be read in order from the start, data items may not be randomly accessed, and there is a slower access of data due to the fact that linked lists are a sequential access data structure. The dynamic nature of a linked list - the fact that they are able to change in size throughout a program's execution, is its primary advantage. 
<br>
##### Space Complexity
O(n)
<br> 
##### Time Complexity
O(n) (Access, Search, Deletion)
<br>
O(1) (Insertion)

<br>
