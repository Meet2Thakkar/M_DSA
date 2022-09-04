class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def inorder(root):
    if root:
        #Travers to left
        inorder(root.left)
        #Travers to root
        print(root.val,end="->")
        #Travers to right
        inorder(root.right)

def postorder(root):
    if root:
        #Travers to root
        print(root.val,end="->")
        #Travers to left
        inorder(root.left)
        #Travers to right
        inorder(root.right)

def preorder(root):
    if root:
        #Travers to left
        inorder(root.left)
        #Travers to right
        inorder(root.right)
        #Travers to root
        print(root.val,end="->")

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.right.left = Node(9)
root.right.right = Node(11)

print("Inorder:")
inorder(root)
print()
print("Postorder:")
postorder(root)
print()
print("Preorder:")
preorder(root)