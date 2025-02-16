def check(s) :
    for i in range(len(s)):
        if s[i] not in ['1', '0', '2']: return False
    return True
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        if check(s) :print("YES")
        else : print("NO")
