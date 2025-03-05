test = int(input())
for _ in range(test):
    n , d = list(map(int , input().split()))
    arr = list(map(int , input().split()))
    for i in range(d , len(arr) , 1):
        print(arr[i] , end = " ")
    for i in range(0 , d):
        print(arr[i] , end = " ")
    print()
