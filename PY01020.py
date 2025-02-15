test = int(input())
for _ in range(test):
    s = input()
    if s[len(s) - 2 : len(s)] == "86":
        print("YES")
    else : print("NO")