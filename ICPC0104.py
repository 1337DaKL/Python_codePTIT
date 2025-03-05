from curses.ascii import isalpha

test = int(input())
for _ in range(test):
    s = list(input())
    for i in range(len(s)):
        if isalpha(s[i]):
            s[i] = " "
    ss = "".join(s)
    arr = list(map(int , "".join(s).split()))
    print(min(arr))
# 2
# 12ab29cd19
# ab123gh456cd