def removeDuplicates(arr):
    left = 0
    for right in range(1, len(arr)):
        if arr[left] != arr[right]:
            left+=1 
            arr[left] = arr[right]
    return left+1 
    
    
arr = [1,2,2,2,3,3,4]
ans = removeDuplicates(arr)
for i in range(ans):
    print(arr[i])
