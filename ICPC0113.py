nt = [True] * (10 ** 6 + 1)
nt[0] = nt[1] = False
for i in range(2 , 10 ** 6 + 1 , 1):
    if nt[i]:
        for j in range(i * i , 10 ** 6 + 1 , i):
            nt[j] = False
def check_dao(s , n):
    if int(s[::-1]) > n : return False
    if s == s[::-1] : return False
    if nt[int(s[::-1])]:
        return True
    return False
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [True] * (n + 1)
        for i in range(n + 1):
            so_dao = int(str(i)[::-1])
            if nt[i] and check_dao(str(i) , n) and arr[i] and arr[so_dao]:
                print(i , so_dao , sep = " " , end = " ")
                arr[i] = False
                arr[so_dao] = False
        print()