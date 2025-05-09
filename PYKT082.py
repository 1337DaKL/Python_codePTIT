def tinhDiemListenAndRead(n):
    if n < 3: return 0
    if n >= 3 and n <= 4: return 2.5
    if n == 5 or n ==6 : return 3
    if n == 7 or n == 8 or n == 9: return 3.5
    if n >= 10 and n <= 12: return 4
    if n >= 13 and n <= 15: return 4.5
    if n >= 16 and n <= 19: return 5
    if n >= 20 and n <= 22 : return 5.5
    if n >= 23 and n <= 26 : return 6
    if n >= 27 and n <= 29: return 6.5
    if n >= 30 and n <= 32 : return 7
    if n >= 33 and n <= 34: return 7.5
    if n >= 35 and n <= 36 : return 8
    if n == 37 or n == 38: return 8.5
    return 9

def tinhDiemIelts(a , b , c , d):
    tongTrungBinh = (a + b + c + d) / 4
    du = tongTrungBinh - int(tongTrungBinh)
    if du < 0.25: return float(int(tongTrungBinh))
    if du >= 0.25 and du < 0.75: return int(tongTrungBinh) + 0.5
    return float(int(tongTrungBinh) + 1)

if __name__ =="__main__":
    test = int(input())
    for _ in range(test):
        a , b , c , d = map(float , input().split())
        print(tinhDiemIelts(tinhDiemListenAndRead(a) , tinhDiemListenAndRead(b) , c , d))

# 2
# 15 25 5.0 5.5
# 22 32 6.0 6.0
