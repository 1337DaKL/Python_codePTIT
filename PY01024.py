def tinhTong(s):
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    return tong

def check(s) :
    if tinhTong(s) % 10 != 0:
        return False
    for i in range(1 , len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != 2:
            return False
    return True

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        if check((s)) : print("YES")
        else : print("NO")