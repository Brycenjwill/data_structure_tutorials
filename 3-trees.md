# Trees

## [Welcome Page](0-welcome.md)

## Visualizing trees
Similar to stacks, trees as a data structure can be visualized as a tree, or a family tree. In a visualized family tree, there is usually some great ancestor who sits at the head of the tree. Then, this granparents children are listed, and below them their own children are listed. 

In a tree, each person would be represented as a node. The top node of the tree (taking the same spot as the ancestor(s) at the top of your family tree) is reffered to as the root node. The nodes connected beneath this top node are referred to as "children nodes" of that top node, and this top node is their "parent node". 

We will mostly be referring to "Binary Trees", where, as the name implies, each node can have at most 2 child nodes.

**Note: Here is a rough ASCII representation of what a binary tree might look like. Note how the branches of the tree form 3 distinct levels.**

             (X)
             / \
           (X) (X)
           / \   \
         (X) (X) (X)
## Why create a Binary Tree?
Because that's the best way to sort a tree. Operations done on a sorted tree (such as adding to the tree, finding a specific node, or removing a node) are efficient. 

For example, lets say this was your tree:

            (10)
             / \
           (5) (14)
           / \   \
         (3) (8) (15)

You could easily figure out where the number 15 is, by realizing that it is greater than the parent node of 10, meaning its on the right half of the tree, and also greater than its child node of 14, putting it on the right half of the children of 14. This means that you often don't have to search half, or even most of the data to find what you are looking for.

## Creating / Inserting into a Binary Search Tree
Here is some code that would create a tree, given an ordered list. 

***Note: The tree will only be sorted if you pass the middle item of a sorted list in first, to create the root node correctly.***

```
class Tree:

    class Node:

        def __init__(self, data):

            self.data = data #The nodes data
            self.left = None #A reference to the left child node
            self.right = None #A reference to the right child node


    def __init__(self):
        self.root = None



    def insert(self, data, node): #Insert new node into tree.
    """
    This method works using recursion. When data is inputted, this method will check if the data is greater or less than the current node. It will recall the function as long as an empty spot has not been found in the data, using node.left / node.right respectively to move left or right down levels of the tree until such a spot is found.
    """

        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                if node.data != data:
                    node.left = Tree.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                if node.data != data:
                    node.right = Tree.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)


#Add nodes to the tree
my_data_sorted = [1,2,3,4,5,6,7,8,9,10]
tree =  Tree()

#Get the middle item of the list to use as the root
root_node = Tree.Node(my_data_sorted[(len(my_data_sorted) // 2)]) 
Tree.insert(root_node)

for data in my_data_sorted:
    #make sure we aren't reentering the root node into the tree.
    if data != my_data_sorted[(len(my_data_sorted) // 2)]: 
        node = Tree.Node(data)
        Tree.insert(data, node)
    
```
***Note: You probably noticed that this algorithm wouldn't work if a duplicate value was given into the tree. In a typical Binary Search Tree, duplicate values are not allowed.***

**Efficiency of inserting into a Binary Search Tree:** O(log(n)). If you are curious about why this is, I recommend looking into the "Binary Search" algorithm, which will explain why insertion in this way would be more efficient than O(n).

## Traversing a Tree in Order
A common question that you will see in regards to a tree is how to traverse it. As you may have noticed, the tree we created is linked together only by its individual nodes, similarly to a linked list. There is no way to traverse to a node other than the root node without first visiting some other node. This is where traversing the tree comes in.

There are 2 common tree traversal methods that will not be discussed here, **Depth First Traversal/Search** and **Breadth First Traversal / Search**. Both of these methods visit every node of a tree, but, importantly, do not do it in order, since they aren't made for that purpose. I recommend reading about both of these methods though, as they are important algorithms with use elsewhere.

The code we used above to create / insert into a tree is similar to what we will do here. This method will return the nodes in order of value. Note that this method would go within the Tree class. Note also that a reverse traversal can be done by simply switching the .left and .right references within the code.

```
def traverse(self, node):
    if node is not None:
        yield from self.traverse(node.left)
        yield node.data
        yield from self.traverse(node.right)
```
**Note that we use the yield keyword, as we want to return more than one set of values. This method should be called with the root (self.root) passed in as the initial node.**

Efficiency: Since we obviously need to visit each node individually, traversing the tree is O(n).

# Problems
Solve these two problems USING STACKS to show that you have learned the data structure.

## Problem 1 (Guided):
I hope you read up on depth first searches as I recommended! Given a Binary Search Tree, write a method that will traverse the tree using a Depth First Search approach, reaching the end of each branch before moving to the next branch. 

Feel free to implement pre, in, or post search. This means that you can "visit" or return the data of a parent node before, or after its children are visited.

            (10)
             / \
           (5) (14)
           / \   \
         (3) (8) (15)

Given this tree, the method would first visit the left branches of 3, 5, and 8, before visiting the right hand side of 15, and 14.

## Solution to Problem 1:
### Walkthrough:
For this solution, we will first create an empty stack. Then, we will add each letter from the word to the end of the stack, in order.
Finally, we will use the pop() method on the stack to remove each item from the stack, starting at the back. We store each item as letter, and add them to a string that will be returned.
# [Solution](1-problem1-solution.py)


## Problem 2:
Create a function that can sort a list using stacks. Two stacks will be required for the solution. For example, if [1,3,5,2,4,6] is passed in, the function will use stacks to sort the list, and will return [1,2,3,4,5,6].

