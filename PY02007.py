dem = 0
set_chia_du = set()
while dem != 10:
    a = list(map(int , input().split()))
    for it in a:
        set_chia_du.add(it % 42)
        dem += 1
print(len(set_chia_du))
# 42 84 252 420 840
# 126 42 84 420 126