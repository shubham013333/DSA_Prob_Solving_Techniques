def removeElement(nums,v):
    left=0
    for right in range(len(nums)):
        if nums[right]!=val:
            nums[left]=nums[right]
            left+=1
    return left  
    
arr = [1,2,2,2,3,3,4]
val = 2
ans = removeElement(arr, val)
for i in range(ans):
    print(arr[i])
print(ans)