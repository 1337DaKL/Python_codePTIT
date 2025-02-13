import math

test = int(input())
for _ in range(test) :
    n , x , m = map(float , input().split())
    nam = 0
    while n < m:
        n = (n + n * x / 100)
        nam += 1
    print(nam)