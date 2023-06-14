class Node:
    def __init__(self,data):
        self.data = data
        self.link = None
a = Node(1)
b = Node(8)
a.link = b
print("This is the Node a: ",a.data)
print("This is the mode b",b.data)
print("Linked node a to be: ",a.link.data)