for _ in range(int(input())):
    arr = [0] * (1001)
    n = int(input())
    for _ in range(n):
        num = int(input())
        arr[num] += 1
    maxo = max(arr)
    for i in range(len(arr)):
        if arr[i] == maxo:
            print(i)
            break
# 3
# 3
# 999
# 999
# 19
# 4
# 13
# 333
# 333
# 13
# 3
# 11
# 12
# 13