class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data

    # Traverse preorder
    def traversePreorder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()
    # Traverse inorder
    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.val, end =' ')
        if self.right:
            self.right.traverseInorder()
    # Traverse postorder
    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()
        if self.right:
            self.right.traversePostorder()
        print(self.val, end=' ')

root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Preorder: ", end='')
root.traversePreorder()
print("Inorder: ", end='')
root.traverseInorder()
print("Postorder: ", end='')
root.traversePostorder()

