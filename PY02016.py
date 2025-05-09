for _ in range(int(input())):
    n = int(input())
    dict_arr = {}
    arr = list(map(int , input().split()))
    for it in arr:
        if it in dict_arr:
            dict_arr[it] += 1
        else:
            dict_arr[it] = 1
    maxo = max(dict_arr.values())
    if maxo <= (n / 2): print("NO")
    else:
        for key in sorted(dict_arr.keys()):
            if maxo == dict_arr[key]:
                print(key)
                break
# 2
# 9
# 3 3 4 2 4 4 2 4 4
# 8
# 3 3 4 2 4 4 2 4