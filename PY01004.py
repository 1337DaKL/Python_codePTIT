import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1 , 1):
        if n % i == 0:
            return False
    return True

test = int(input())  # Nhập số lần cần kiểm tra2

for _ in range(test):  # Lặp qua số lần nhập dữ liệu
    n = int(input())  # Nhập một số cần kiểm tra
    dem = 0
    for i in range(1, n + 1 , 1):  # Tính từ 2 đến căn bậc 2 của n
        if math.gcd(n, i) == 1:  # Kiểm tra nếu i và n không có ước chung nào ngoài 1
            dem += 1
    if is_prime(dem):  # Kiểm tra xem dem có phải là số nguyên tố không
        print("YES")
    else:
        print("NO")
