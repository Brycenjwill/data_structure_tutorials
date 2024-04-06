class Tree:

    class Node:
        def __init__(self, data):

            self.data = data #The nodes data
            self.left = None #A reference to the left child node
            self.right = None #A reference to the right child node


    def __init__(self):
        self.root = None

    def insert(self, data, node = None): #Insert new node into tree.
        if self.root == None:
            self.root = Tree.Node(data)

        #Set node to root if one isn't selected already
        elif node == None:
            node = self.root

        elif data < node.data:
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



    def depth_first_search(self):
        yield from self.traverse_forward(self.root)

    #Solution starts here -------------
    #Note that my solution will be using post-order.
    def traverse_forward(self, node):
        if node is not None:
            yield from self.traverse_forward(node.left)
            yield node.data
            yield from self.traverse_forward(node.right)

#Add nodes to the tree
my_data_sorted = [1,2,3,4,5,6,7,8,9,10]
tree =  Tree()

#Get the middle item of the list to use as the root

tree.insert(my_data_sorted[(len(my_data_sorted) // 2)])

for data in my_data_sorted:
    #make sure we aren't reentering the root node into the tree.
    if data != my_data_sorted[(len(my_data_sorted) // 2)]: 
        tree.insert(data)


#Test results to make sure all nodes are visited
print(tree.depth_first_search())