n = int(input())

for i in range(n):
    n2 = int(input())
    arr = list(map(int, input().split(' ')))[:n2]
    for item in arr:
        if arr.count(item) == 1:
            ans = arr.index(item) + 1
            print(ans)