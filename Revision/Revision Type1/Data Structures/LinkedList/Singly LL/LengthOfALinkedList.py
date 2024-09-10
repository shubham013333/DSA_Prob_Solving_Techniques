class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
def length_Lnked_List(head):
    cnt = 0
    temp = head 
    while temp is not None:
        temp = temp.next 
        cnt+=1
    return cnt 
arr = [2, 5, 8, 7]
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])


ans = length_Lnked_List(head)

print(ans)