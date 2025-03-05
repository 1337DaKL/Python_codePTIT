from math import *
def is_prime(n):
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0 : return False
    return n > 1
if __name__ == "__main__":
    n , m = list(map(int , input().split()))
    arr = []
    for _ in range(n):
        arr_tmp = list(map(int , input().split()))
        arr.append(arr_tmp)
    for i in range(n):
        for j in range(m):
            if is_prime(arr[i][j]):
                arr[i][j] = 1
            else:
                arr[i][j] = 0
    for i in range(n):
        for j in range(m):
            print(arr[i][j] , end = " ")
        print()
