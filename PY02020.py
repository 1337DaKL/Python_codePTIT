n = int(input())
arr = list(map(float , input().split()))
maxo = max(arr)
mino = min(arr)
tong  = 0
dem = 0
for it in arr:
    if maxo != it and mino != it: 
        tong += it
        dem += 1
trung_binh = tong / dem
print("%.2f" %trung_binh)