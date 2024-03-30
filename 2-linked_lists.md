# Linked Lists

## [Welcome Page](0-welcome.md)

## Lists vs Linked Lists
This tutorial assumes that you understand Python's List data structure. Like a list, a linked list is made up of several items. Unlike a list, however, a linked list is not accessed via indexes. In fact, if you want to find the nth item in a linked list, you would have to traverse the linked list until you reached that item. 

## Memory
In most languages, the items of a list or array are stored within a set space in memory. Many times in a language like C, ,you have to make sure that the program knows just how much space an array will need. A linked list does not function in this way.
So how does this work? Each item in a linked list is made of two parts, its data, and a "pointer" to the next item in the linked list. A pointer is typically a reference to a point in memory, however, since python does not have pointers, wee will instead have this section be a direct reference to the next item in the linked list. 
**Note: Each item in a linked list is referred to as a.**


## The Head
So if the items in a linked list aren't stored together in memory, and can only be accessed by a reference from the previous item, then how do we know where the beginning of a linked list is? This is where the head comes in. 
Each linked list has head, which is a reference its first item. Once we have the head, we can now traverse to any item in the linked list.

## The Tail
One last thing before we go over some code for working with linked lists, we need to know where the list ends. This is important, since the last item in a linked list won't hold a reference to the next item in the list, since their isn't one. This is referred to as the tail of the linked list. 

## Creating a Linked List
Python has no built in linked list data structure. We will need to create a class for the nodes of the linked list, and one for the linked list itself so that we can keep track of the head and tail of the linked list. This code would work:
```
class LinkedList():
    class Node():
        def init(self, data): #Initializing a node
            self.data = data
            self.next = none #initialize the next element of the node as empty

    def init(self):
        self.head = none #Initialize head and tail as none to start
        self.tail = none
```

## Inserting into a Linked List
To use a linked list, we will obviously need to know how to add to a linked list. There area  few cases that need to be handled;

1: What should happen when we want to insert into the beginning of a linked list
2: What should happend if we want to insert into the end of a linked list
3: What shoudl happen if we want to insert into somewhere in the middle of a linked list

### Inserting to the beginning of the Linked List
We need to make sure that we set the new head for the linked list. 
```
#Within the LinkedList class. . .
def insertHead(self, data): #Update the head for the linked list
    new node = LinkedList.node(data) #Create the new node

    # If the list is empty, then point both head and tail
    # to the new node.
    if self.head is None:
        self.head = new_node
        self.tail = new_node

    # If the list is not empty, then only self.head will be
    # affected.
    else:
        new_node.next = self.head # Connect new node to the previous head
        self.head.prev = new_node # Connect the previous head to the new node
        self.head = new_node      # Update the head to point to the new node
```
Efficiency: Adding to the beginninf of a linked list is O(1)

### Inserting to the end of a Linked List
We need to make sure that we set the new tail for the linked list. 
```
#Within the LinkedList class. . .
def insert_tail(self, value):
    """
    Insert a new node at the back (i.e. the tail) of the 
    linked list.
    """
    new_node = LinkedList.Node(value)  

    if self.head is None: #If the list was empty, then we also need to set the head of the linked list. . .
        self.head = new_node
        self.tail = new_node

    # If the list is not empty, then only self.tail will be
    # affected.
    else:
        new_node.prev = self.tail # Connect new node to the previous tail
        self.tail.next = new_node # Connect the previous tail to the new node
        self.tail = new_node      # Update the tail to point to the new node
```
Efficiency: Inserting into the end of a linked list is O(1) in the best case (Where there are 0 items in the list) or O(n) at worst if there are more items in the linked list. 

### Inserting into the middle of a Linked List
This is where things get trickier. Here, we will be insertingo into a linked list, after some given value. We will need to traverse the linked list, using node.next, and then change the reference of the item after which we are to insert to the new node, and the after of the new node to where the previous node was pointing. 

```
#Within the LinkedList class. . .
def insert(self):
    # Search for the node that matches 'value' by starting at the 
    # head of the list.
    
    curr = self.head #Start with the head of the linked list

    while curr is not None: 
        if curr.data == value:
            # If the location of 'value' is at the end of the list,
            # then we can call insert_tail to add 'new_value'
            if curr == self.tail:
                self.insert_tail(new_value)
            # For any other location of 'value', need to create a 
            # new node and reconenct the links to insert.

            else:
                new_node = LinkedList.Node(new_value)
                new_node.prev = curr       # Connect new node to the node containing 'value'
                new_node.next = curr.next  # Connect new node to the node after 'value'
                curr.next.prev = new_node  # Connect node after 'value' to the new node
                curr.next = new_node       # Connect the node containing 'value' to the new node
            return # We can exit the function after we insert
        curr = curr.next # Go to the next node to search for 'value'
```
Efficiently: Adding to the middle of a linked list is O(n)

## Removing From a Linked List
Lets assume that we need to remove a item from a linked list, and that we have the value of the item we want to remove. We need to make sure that we don't destroy the integrity of the linked list, by making sure that the linked list retains a head, a tail, and that each item within the linked list are linked appropriately. 

Here is a sample of some code that would fulfill that functionality. . .
```
#Within the LinkedList class. . .

def remove(self, value):

    current = self.head

    # Loop until we have reached the end (None)
        while current is not None:
            if current.data == value and current == self.tail: #Check that we aren't dealing with the tail...
                if self.head == self.tail: #If only one item in list
                    self.head = None
                    self.tail = None
                elif self.tail is not None: #Double check that there is a tail to remove. . .
                    self.tail.prev.next = None #unlink second from end from prev tail
                    self.tail = self.tail.prev  #Set new tail.
                break

            elif current.data == value and current == self.head: #Check that we aren't dealing with the head...
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                # If the list has more than one item in it, then only self.head
                # will be affected.
                elif self.head is not None:
                    self.head.next.prev = None  # Disconnect the second node from the first node
                    self.head = self.head.next  # Update the head to point to the second node
                break

            elif current.data == value: #if we've found the value we are looking for and its somewhere in the middle. . .
                current.next.prev = current.prev
                current.prev.next = current.next #replace next values as needed
                break
            current = current.next
```
Efficiency: Removing from a linked list is O(n), since we need to search n items in the list to find the one we need to remove


# Problems
Solve these two problems USING LINKED LISTS to show that you have learned the data structure.

## Problem 1 (Guided):
Reverse a linked list. This is an interview question that has stressed me out in the past, so I will guide you on ways to do this.

## Solution to Problem 1:
### Walkthrough:
We will assume that a linked list is created already, as is in the 2-problem1-solution.py file linked below.
So, we will start by grabbing the current head of the linked list, and setting cur to this value. cur will always store the node we are currently looking at. Next, we will initialize a prev value as None. This prev value will "remember" the item that we looked at last. We will also make sure to store the tail as the current head.

We will then loop through the linked list, starting with the head. On each iteration, we will first set a next variable to the current node.next. You may be wondering why we do this. The reason is that since we will be altering the linked list in place, and will not be creating a new linked list, we need to remember the old node.next before we alter the current node.
Next, we will set the cur.next to the prev variable. As you could guess, this will set the next of the head node to None, which is what we want, since the old head will be the new tail. Then, we will set the prev to cur, since we are done processing the current node, and we will move along the linked list until we reach the end.

Once the end is reached, we simply set the head to the current node, and thats it! 
# [Solution](2-problem1-solution.py)


## Problem 2:
Given a linked list, create a method that removes duplicate values from the linked list. As a bonus, return the number of duplicate values in the linked list.

