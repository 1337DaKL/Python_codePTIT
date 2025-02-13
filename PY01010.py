def kiemtra(s) :
    if(s[0:2] == s[len(s) - 2 : len(s)]) :
        return True
    return False
if __name__ == "__main__" :
    test = int(input())
    for _ in range(test):
        s = input()
        if kiemtra(s) :
            print("YES")
        else :
            print("NO")