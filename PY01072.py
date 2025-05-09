n, k = 0, 0
a = [0] * 100
check = False
def khoi_tao():
    for i in range(1 , k + 1):
        a[i] = i
def sinh():
    global check
    i =  k
    while i > 0 and a[i] == n - k + i:
        i -= 1
    if i == 0:
        check = True
    else:
        a[i] +=  1
        for j in range(i + 1, k + 1 , 1):
            a[j] = a[j -1] + 1
if __name__ == "__main__":
    nn , k = list(map(int , input().split()))
    arr = list(map(int , input().split()))
    set_arr = set(arr)
    arr_tmp = []
    for it in set_arr:
        arr_tmp.append(it)
    n = len(arr_tmp)
    khoi_tao()
    while check == False:
        for i in range(1 , k + 1):
            print(arr_tmp[a[i] - 1] , end = " ")
        print()
        sinh()