from math import *
check = True
a, K, N = map(int , input().split())
for i in range(1 , int(N / K) + 1 , 1) :
    if((i * K) - a > 0) :
        check = False
        print(i * K - a , end=" ")
if check:
    print(-1)
else:
    print()