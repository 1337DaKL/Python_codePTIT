n = int(input())
arr =[]
for i in range(n):
    arr_tmp = list(map(int, input().split()))
    arr.append(arr_tmp)
k = int(input())
nua_tren = 0
nua_duoi = 0
for i in range(n):
    for j in range(n):
        if j > i: nua_tren += arr[i][j]
        elif i > j: nua_duoi += arr[i][j]
chenh_lech = abs(nua_duoi - nua_tren)
if chenh_lech <= k: print("YES")
else: print("NO")
print(chenh_lech)