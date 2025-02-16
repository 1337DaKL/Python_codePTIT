def sinhThuanNghichChan():
    arr = []
    for i in "2468":
        arr.append(int(i + i))
    for i in "2468":
        for j in "02468":
            arr.append(int(i + j + j + i))
    for i in "2468":
        for j in "02468":
            for k in "02468":
                arr.append(int(i + j + k + k + j + i))
    return sorted(arr)
def check(n , arr):
    sKetQua = ""
    for i in range(len(arr)) :
        if arr[i] < n: sKetQua += (str(arr[i]) + " ")
    return sKetQua
if __name__ == "__main__":
    arr = sinhThuanNghichChan()
    test = int(input())
    for _ in range(test):
        n = int(input())
        print(check(n , arr))