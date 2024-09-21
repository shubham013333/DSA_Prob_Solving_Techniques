def isSorted(nums,n):
    for i in range(1, n):
        if nums[i]<nums[i-1]:
            return False 
        return True 


nums = [10,2,3,9]
n = len(nums)

ans = isSorted(nums,n)
print(ans)