test = int(input())
for _ in range(test):
    s = input()
    for i in range(int(len(s) / 2)):
        cnt = int(s[i * 2 + 1])
        while cnt > 0:
            print(s[i * 2] , end="")
            cnt -= 1
    print()