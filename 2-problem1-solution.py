class LinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None



    #Setup code so we can create the linked list
    #--------------------------------------------------------------------------------------------------
    def insertHead(self, data): #Update the head for the linked list
        new_node = LinkedList.Node(data) #Create the new node

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

    def insert(self, value, new_value):
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

        #Print the items of the linked list for testing
    def display(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

#Solution Begins Here------------------------------------------------------------------
    def reverse(self): #This method will reverse the linked list
        prev = None #How we will keep track of the last node visted
        cur = self.head #The current node we are visitng
        self.tail = cur
        while cur != None: 
            next = cur.next #Keep track of the next item in the list. We store this in a variable, 
            #since we will be changing the cur.next soon
            cur.next = prev #We need to swap the next of the current item to the previous item, to switch their positioning in the list
            prev = cur #Set the previous item to the current item
            cur = next #Move to the next item in the list

        self.head = prev #Finally, we set the new head to the old final item of the list



#Creating the linked list to test with
#------------------------------------------------------------------------------------------
linkedList = LinkedList()
linkedList.insertHead(1)
linkedList.insert(1, 2)
linkedList.insert_tail(3)
print("Starting Linked List: ")
linkedList.display()
print()
#Test the method. . .
linkedList.reverse()
print("Reversed Linked List: ")
linkedList.display()