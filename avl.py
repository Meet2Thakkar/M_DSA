import sys

# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AvlTree(object):

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height    
    
    # Get balance factor of node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right # y is x.right which is y in example
        T2 = y.left # T2 is beta of y
        y.left = z # Now y.right = x
        z.right = T2 # x.right is beta
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    # Function to insert a node
    def insert_node(self, root, key):
        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to delete node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            if root.left:
                root.left = self.delete_node(root.left, key)
            else:
                print("Given Node not found")
        elif key > root.key:
            if root.right:
                root.right = self.delete_node(root.right, key)
            else:
                print("Given Node not found")
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the Tree
        if balanceFactor > 1:
                if self.getBalance(root.left) >= 0:
                    return self.rightRotate(root)
                else:
                    root.left = self.leftRotate(root.left)
                    return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def inorder(self, root):
            if root is not None:
                self.inorder(root.left)
                print(str(root.key) + "->", end = ' ')
                self.inorder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "|    "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

myTree = AvlTree()
root = None
nums = [33,13,52,9,21,61,8,11]
for num in nums:
    root = myTree.insert_node(root, num)
print("Inorder traversal: ", end= ' ')
myTree.inorder(root)
print(" ")
myTree.printHelper(root, "", True)
key = 13
print("\nDelete 13")
root = myTree.delete_node(root, key)

print("After Deletion: ", end= ' ')
myTree.inorder(root)
print(" ")
myTree.printHelper(root, "", True)