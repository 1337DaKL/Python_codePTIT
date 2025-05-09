from math import *
def kiem_tra_so_nguyen_to  (n):
    for i in range(2 , isqrt(n) + 1):   
        if n % i == 0: return False
    return n > 1
if __name__ == "__main__":
    pre = []
    for i in range(2 , 10 ** 6 + 1 , 1):
        if len(pre) == 1000:
            break
        if kiem_tra_so_nguyen_to(i):
            pre.append(i)
    n , x = list(map(int , input().split()))
    ans = [x]
    print(ans[0] , end = " ")
    for i in range(0 , n):
        tong = ans[i] + pre[i]
        ans.append(tong)
        print(tong ,end = " ")
