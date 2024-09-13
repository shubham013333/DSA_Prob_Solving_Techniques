arr = [3,2,1,5,2]

largest = arr[0]

for i in range(len(arr)):
    if arr[i] >largest:
        largest = arr[i]

print(largest) 