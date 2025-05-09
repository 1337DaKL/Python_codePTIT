test = int(input())
for _ in range(test):
    arr= list(map(int , input().split()))
    maxo = max(arr)
    mino = min(arr)
    x1 =input().strip()
    x2 = input().strip()
    x1_min = x1.replace(str(maxo) , str(mino))
    x2_min = x2.replace(str(maxo) , str(mino))
    x1_max = x1.replace(str(mino) , str(maxo))
    x2_max = x2.replace(str(mino) , str(maxo))
    print(int(x1_min) + int(x2_min) , int(x1_max) + int(x2_max) , sep = " " , end = "\n")
# 1
# 5 6
# 645 
# 666