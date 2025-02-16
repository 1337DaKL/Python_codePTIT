from operator import truediv


def soTangGiam(s) :
    if len(s) < 3 : return  False
    dinh = -1
    for i in range(len(s) - 1) :
        if int(s[i]) < int(s[i + 1]) :
            continue
        elif int(s[i]) > int(s[i + 1]):
            dinh = i
            break
        else :
            return False
    if dinh == -1 or dinh == 0: return False
    for i in range(dinh , len(s) - 1 , 1) :
        if s[i] <= s[i + 1] :
            return False
    return True
if __name__ == "__main__" :
    test = int(input())
    for _ in range(test) :
        s = input()
        if soTangGiam(s) :
            print("YES")
        else :
             print("NO")

