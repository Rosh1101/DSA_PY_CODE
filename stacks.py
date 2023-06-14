'''stack = []
def register(s,element):
    s.append(element)
def remove(s):
    if isEmpty(s):
        return "Empty"
    return s.pop()
def peek(s):
    if isEmpty(s):
        return "Empty"
    return stack[len(s)-1]
def size(s):
    return len(s)
def isEmpty(s):
    return size(s) == 0

while True:

    n = int(input("\n_>"))
    if(n==1):
        register(stack,int(input("Enter the number to insert: ")))
        print(stack)

    elif(n==2):
        remove(stack.pop())
        print(stack)
    elif(n==3):
        peek(stack)
        print(stack)
    elif(n==4):
        size(stack)
        print(stack)
    else:
        print("Error input :(")
'''

stack = []

def push(s,item):
    s.append(item)

def remove(s):
    if isEmpty(s):
        return 'No element present'
    return s.pop()

def isEmpty(s):
    return length(s)

def length(s):
    return len(s) == 0

while True:
    n = input("Enter the operation to perform: ")
    if(n=='+'):
        push(stack,int(input("Enter the number to push: ")))
        print(stack)
    elif(n=='-'):
        remove(stack.pop())
        print(stack)
    elif(n=='!'):
        isEmpty(stack)
        print(stack)
