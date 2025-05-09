n = int(input())
arr = list(map(int , input().split()))
dem = 0
for i in range( 1 ,len(arr)):
    if arr[i] != arr[i - 1]: dem += 1
print(dem)
# 6
# 1 0 0 1 1 1