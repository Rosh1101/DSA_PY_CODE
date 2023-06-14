class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
root = BinaryTreeNode("Root")
left = BinaryTreeNode("left")
right = BinaryTreeNode("Right")

root.left = left
root.right = right
print(root.left.data)