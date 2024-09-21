class Node:
    def __init__(self, data1,next1 =None):
        self.data = data1
        self.next = next1

def ShowLinkedList(head):
    while head is not None:
        print(head.data)
        head = head.next

def insertAtBegining(head, val):
    temp = Node(val, head)
    return temp

arr = [2,3,4]
val = 1 

head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])

head = insertAtBegining(head, val)
ShowLinkedList(head)