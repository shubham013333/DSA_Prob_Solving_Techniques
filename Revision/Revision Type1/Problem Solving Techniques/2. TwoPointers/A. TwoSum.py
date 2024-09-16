def t2_sum(arr, target):
    left = 0
    right = len(arr) - 1 
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return arr[left],arr[right]
        elif current_sum < target:
            left+=1 
        else:
            right-=1 
    return None

nums = [1,2,3,4,6]
target = 6
ans = t2_sum(nums, target)
print(ans)