def soChuSoKhacNhau(s):
    arr = 10 * [0]
    for i in range(len(s)):
        arr[int(s[i])] += 1
    count = 0
    for i in range(10):
        if arr[i] != 0 :
            count += 1
    if count != 2 : return False
    return True

def kiemTraSoDep(s) :
    if soChuSoKhacNhau(s) == False: return False
    for i in range(0 , len(s) - 2) :
        if s[i] != s[i + 2] :
            return  False
    return True

if __name__ == "__main__" :
    test = int(input())
    for _ in range(test) :
        s = input()
        if kiemTraSoDep(s) :
            print("YES")
        else : print("NO")