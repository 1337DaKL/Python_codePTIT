from math import *
def test (s) :
    for i in range(1 ,len(s)):
        kcs1 = ord(s[i]) - ord(s[i - 1])
        kcs2 = ord(s[len(s) - i - 1]) - ord(s[len(s) - i])
        if abs(kcs1) != abs(kcs2):
            return False
    return True
if __name__ == "__main__":
    t = int(input())
    for _ in range(t) :
        s = input()
        if test(s) :
            print("YES")
        else :
            print("NO")