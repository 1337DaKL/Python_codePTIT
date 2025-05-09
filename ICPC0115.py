arr = [1] * 10
for i in range(1 , len( arr)):
    arr[i] = arr[i - 1] * i
for _ in range(int(input())):
    s = input()
    tong_giai_thua = 0
    for i in s:
        tong_giai_thua += arr[int(i)]
    if tong_giai_thua == int(s): print("Yes")
    else: print("No")
# 2
# 145
# 235