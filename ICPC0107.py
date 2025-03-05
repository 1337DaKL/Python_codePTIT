test = int(input())
for _ in range(test):
    arr = list(map(int , input().split()))
    mino = min(arr)
    maxo = max(arr)
    x1 , x2 = "", ""
    a = list(input().split())
    if len(a) == 1:
        x1 = a[0]
        x2 = input()
    else:
        x1 = a[0]
        x2 = a[1]
    maxo_swaped = int(x1.replace(str(mino) , str(maxo))) + int(x2.replace(str(mino) , str(maxo)))
    mino_swaped = int(x1.replace(str(maxo) , str(mino))) + int(x2.replace(str(maxo) , str(mino)))
    print(mino_swaped , maxo_swaped , sep = " " , end = "\n")