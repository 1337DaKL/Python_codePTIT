nt = [True] * (10 ** 6 + 1)
nt_triplet = [0] * (10 ** 6 + 8)
nt[0] = nt[1] = False
for i in range(2 , 10 ** 6 + 1 , 1):
    if nt[i]:
        for j in range(i * i , 10 ** 6 + 1 , i):
            nt[j] = False
for i in range(2 , 10 ** 6 + 1):
    if i + 6 < 10 ** 6:
        if nt[i] and nt[i + 2 ] and nt[i + 6]:
            nt_triplet[i + 7] += 1
        if nt[i] and nt[i + 4] and nt[i + 6]:
            nt_triplet[i + 7] += 1
for i in range(1  , 10 ** 6 + 8):
    nt_triplet[i] += nt_triplet[i - 1]



for _ in range(int(input())):
    print(nt_triplet[int(input())])