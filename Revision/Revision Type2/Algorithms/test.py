def hammingDistance(bin_str, A, B):
    if not all(char in '01' for char in bin_str):
        return "INVALID"
    
    n = len(bin_str)
    count_0 = bin_str.count('0')
    count_1 = n - count_0

    rearranged_01 = '0' * count_0 + '1' * count_1
    rearranged_10 = '1' * count_1 + '0' * count_0

    hamming_01 = sum(1 for i in range(n) if bin_str[i] != rearranged_01[i])
    hamming_10 = sum(1 for i in range(n) if bin_str[i] != rearranged_10[i])

    cost_01 = count_0 * count_1 * B
    cost_10 = count_0 * count_1 * A

    if cost_01 < cost_10:
        return hamming_01
    elif cost_10 < cost_01:
        return hamming_10
    else:
        return min(hamming_01, hamming_10)


input_data = []
T = int(input().strip())

for _ in range(T):
    bin_str = input().strip()
    A, B = map(int, input().strip().split())
    input_data.append((bin_str, A, B))

for bin_str, A, B in input_data:
    if not all(char in '01' for char in bin_str):
        print("INVALID")
        continue
        
    result = hammingDistance(bin_str, A, B)
    print(result)


