def kiem_tra_day_so_phu_hop(a1 , a2):
    a1 = list(a1)
    a2 = list(a2)
    a1.sort()
    a2.sort()
    for i in range(len(a1)):
        if a1[i] > a2[i]: return False
    return True
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a1 = list(map(int , input().split()))
        a2 = list(map(int , input().split()))
        if kiem_tra_day_so_phu_hop(a1 , a2):
            print("YES")
        else: print("NO")
# 2
# 4
# 7 5 3 2
# 5 4 8 7
# 8
# 7 5 3 2 5 105 45 10
# 2 4 0 5 6 9 75 84