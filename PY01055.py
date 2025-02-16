def kiemTraSoXenKe(s):
    if len(s) % 2 == 0 : return False
    if s[0] == s[1]: return False
    for i in range(2 , len(s) , 2):
        if s[i] != s[0] : return False
    return True
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        if kiemTraSoXenKe(s): print("YES")
        else: print("NO")
# 2
# 2324272921262
# 13141516