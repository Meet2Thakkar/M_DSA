class newNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

# Calculate the depth
def calculateDepth(node):
    d = 0
    while(node is not None):
        d += 1
        node = node.left
    return d

# This function tests if a binary tree
# is perfect or not. It basically checks
# for two things :
# 1) All leaves are at same level
# 2) All internal nodes have two children
def isPerfectRec(root, d, level=0):
    # An empty tree is perfect
    if (root == None):
        return True
    # Check the presence of tree
    # If leaf node, then its depth must
    # be same as depth of all other leaves.
    if (root.left is None and root.right is None):
        return (d == level + 1)
    # If internal node and one child is empty
    if (root.left is None or root.right is None):
        return False
    # left and right substream must be perfect
    return (isPerfectRec(root.left, d, level + 1) and isPerfectRec(root.right, d, level + 1))

# Wrapper over isPerfectRec()
def isPerfect(root):
    d = calculateDepth(root)
    return isPerfectRec(root, d)

root = None
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
#root.right.right = newNode(7)

if (isPerfect(root)):
    print("YES it is PBT")
else:
    print("NO it is not PBT")
    