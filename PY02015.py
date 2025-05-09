while True:
    a , b , c , d = list(map(int , input().split()))
    if a==b==c==d==0:
        break
    dem = 0
    while not a==b==c==d:
        a_tmp = a
        a = abs(a - b)
        b = abs(b - c)
        c = abs(c - d)
        d = abs(d - a_tmp)
        dem += 1
    print(dem)
# 1 3 5 9
# 4 3 2 1
# 0 0 0 0