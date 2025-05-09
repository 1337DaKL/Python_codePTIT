def kiemTraThangBang(s):
    for i in range(0 , len(s) - 1, 1):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(s[len(s) - i - 1]) - ord(s[len(s) - i - 2])): return False
    return True
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        if kiemTraThangBang(s): print("YES")
        else : print("NO")
# 2
# acxz
# bcxz