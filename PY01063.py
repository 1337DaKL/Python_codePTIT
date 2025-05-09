def demSoTrongXau(s , n):
    count = 0
    while s.find(n) != -1:
        count+= 1
        index = s.find(n)
        s = s[index + len(n) + 1: ]
    return count
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        n = input()
        print(demSoTrongXau(s, n))
# 2
# 1212121112211221121
# 121
# 2222222222322292
# 2222