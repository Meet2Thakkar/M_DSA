class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#Inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end=' ')
        inorder(root.right)

# Insert Node
def insert(node, key):
    # Return a new node if node is empty
    if node is None:
        return Node(key)
    
    # Traverse to the position and insert the node
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

# Find inorder successor
def minValueNode(node):
    current = node

    # Find the leftmost tree
    while(current.left is not None):
        current = current.left
    return current

# Deleting a Node
def deleteNode(root, key):
    if root is None:
        return root
    
    # Find the node to be deleted
    if key < root.key:
        if root.left:
            root.left = deleteNode(root.left, key)
        else:
            print("Given Node not found")
    elif(key > root.key):
        if root.right:
            root.right = deleteNode(root.right, key)
        else:
            print("Given node not found")
    else:
        # If the Node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None 
            return temp
        # If the Node has 2 children
        # Place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)
        
        root.key = temp.key 

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
    
    return root

root = None
root = insert(root, 8)
root = insert(root, 10)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 4)
root = insert(root, 11)
root = insert(root, 9)

print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 100")
root = deleteNode(root, 100)

print("\nDelete 4")
root = deleteNode(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)
