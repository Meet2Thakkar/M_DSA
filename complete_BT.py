class Node:

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

#count the number of nodes
def count_nodes(root):
    if root is None:
        return 0
    return (1 + count_nodes(root.left) + count_nodes(root.right))

# Check if the tree is complete binary tree
def is_complete(root, index, numberNodes):

    # Check if the tree is empty
    if root is None:
        return True

    if index >= numberNodes:
        return False
    # The element in the index 2i+1 will become the left child and element in 2i+2 index will become the right child
    return (is_complete(root.left, 2*index + 1, numberNodes) and is_complete(root.right, 2*index + 2, numberNodes))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#root.right.left = Node(6)
root.right.right = Node(7)

node_count = count_nodes(root)
index = 0

if is_complete(root, index, node_count):
    print("Tree is Complete BT")
else:
    print("Tree is not Complete BT")