arr = [1,2,3,4,5,6]
l = 2
r = 5
n = len(arr)
prefix_sum =[0] *n
prefix_sum[0] = arr[0]

for i in range(len(arr)):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
    
if l == 0:
    print(prefix_sum[r])
else:
    print(prefix_sum[r] - prefix_sum[l-1])