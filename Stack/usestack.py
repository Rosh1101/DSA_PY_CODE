from stack import Stack

s = Stack()
s.push(9)
s.push(6)

while s.isEmpty() is False:
    print(s.pop())