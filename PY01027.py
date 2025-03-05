def soLocPhatDep(s):
    cnt = 0
    for i in s:
        if s != "6" or s != "8" : return False
        if s == "8" : cnt += 1
        else : cnt = 0
        if cnt == 3: return False
    return True

if __name__ == "__main__":
    s = input()
    if soLocPhatDep(s) : print("YES")
    else: print("NO")