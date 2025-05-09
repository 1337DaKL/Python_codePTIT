def kiemTra(s):
    a = s.split(".")
    if len(a) != 4: return False
    for i in range(len(a)):
        if not a[i].isdigit() or(a[i] != "0" and a[i][0] == "0") : return False
        if int(a[i]) < 0 or int(a[i]) > 255: return False
    return True
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        if kiemTra(s): print("YES")
        else: print("NO")

# 2
# 192.168.1.1
# 256.255.255.255