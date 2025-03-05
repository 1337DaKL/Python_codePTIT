test = int(input())
for _ in range(test):
    s = list(input())
    for i in range(len(s)):
        if s[i].isalpha():
            s[i] = " "
    arr = list(map(int , "".join(s).split()))
    print(max(arr))
# 2
# 12ab29cd19
# ab123gh456cd