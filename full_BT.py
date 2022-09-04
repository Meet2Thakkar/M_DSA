class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

# Checking full binary tree
def isFullTree(root):
    # Tree empty case
    if root is None:
        return True

    # Checking whether child is present
    if root.left is None and root.right is None:
        return True
    
    if root.left is not None and root.right is not None:
        return (isFullTree(root.left) and isFullTree(root.right))
    
    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
#root.left.left.right = Node(9)

if isFullTree(root):
    print("The Tree is full binary")
else:
    print("The Tree is not full binary")