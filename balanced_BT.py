class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class Height:
    def __init__(self):
        self.height = 0

def is_balanced(root, height):
    left_height = Height()
    right_height = Height()
    # Check if tree is empty or not
    if root is None:
        return True
    
    l = is_balanced(root.left, left_height)
    r = is_balanced(root.right, right_height)

    height.height = max(left_height.height, right_height.height) + 1

    if abs(left_height.height - right_height.height) <= 1:
        return l and r

    return False

height = Height()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
#root.right.left.left = Node(8)

if is_balanced(root, height):
    print('The tree is balanced')
    print(f"height of tree is : {height.height}")
else:
    print('The tree is not balanced')