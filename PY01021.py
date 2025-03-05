from curses.ascii import isdigit, isalpha

test = int(input())
for _ in range(test):
    s = input()
    arr = list()
    tong = 0
    for i in range(len(s)):
        if isalpha(s[i]):
            arr.append(s[i])
        if isdigit(s[i]):
            tong += int(s[i])
    arr.sort()
    for i in range(len(arr)):
        print(arr[i] , end = "")
    print(tong)