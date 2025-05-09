n = int(input())
arr = []
for _ in range(n):
    arr_tmp = list(map(int , input().split()))
    arr.append(arr_tmp)
k = int(input())
nua_tren, nua_duoi = 0, 0
for i in range(n):
    for j in range(n):
        if i < n - j - 1:
            nua_tren += arr[i][j]
        elif i > n - j - 1:
            nua_duoi += arr[i][j]
do_chenh_lech = abs(nua_tren - nua_duoi)
if do_chenh_lech <= k : print("YES")
else: print("NO")
print(do_chenh_lech)