n = int(input())
arr = list(map(int , input().split()))
arr_check = [False] * (n + 1)
arr_check[0] = True
for it in arr:
    if it <= n :
        arr_check[it] = True
check = True
for i in range(len(arr_check)):
    if arr_check[i] == False:
        check = False
        print(i)
        break
if check:
    print(n + 1)