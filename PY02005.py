n = int(input())
a = list(map(int , input().split()))
dem = 0
for i in range(len(a)):
    for j in range( i):
        if a[j] > a[i]:
            dem += 1
print(dem)