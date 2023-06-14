'''class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("None")
    return
def takeInput():
    inputList = [element for element in input().split()]
    head = None
    for currentDta in inputList:
        if currentDta == -1:
            break
        newNode=Node(current)
        if head is None:
            head = newNode
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = newNode
    return head
head = takeInput()
printLL(head)'''





class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLL(head):
    while head is not None:
        print(str(head.data)+"-->",end="")
        head=head.next
    print("None")
    return
def takeInput():
    inputList=[int (ele) for ele in input().split()]
    head=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head=newNode
        else:
            curr=head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
    return head
head=takeInput()
printLL(head)