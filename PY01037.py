def soCanTim(n):
    dem = 0
    while dem <= 1000 :
        if n % 7 == 0:
            return n
        n = n + int(str(n)[::-1])
        dem += 1
    return -1
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n = int(input())
        print(soCanTim(n))