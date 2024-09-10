class Node:
    def __init__(self, data1,next1 = None):
        self.data = data1
        self.next = next1
        
        
def printLL(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next 
def deleteatend(head):
    if head is None or head.next is None:
        return None
        
    temp = head
    
    while temp.next.next is not None:
        temp = temp.next 
        
    temp.next = None
    
    return head
    
    
arr = [2,3,4]


head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])

head = deleteatend(head)
printLL(head)