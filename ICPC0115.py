arr = [0] * (10 ** 8 + 1)
giai_thua = 1
for i in range(1 , 10 ** 8 , 1):
    giai_thua *= i
    arr[i] = giai_thua

def kiem_tra_krish(s):
    tong_giai_thua = 0
    for i in range(len(s)):
        tong_giai_thua += arr[int(s[i])]
    if tong_giai_thua == int(s) : return True
    return False
if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        if kiem_tra_krish(s): print("Yes")
        else: print("No")
# 2
# 145
# 235