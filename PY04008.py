class Matrix:
    def __init__(self, n, m, arr):
        self.n = n
        self.m = m
        self.arr = arr
    def ma_tran_chuyen_vi(self):
        ma_tran_chuyen_vi = [[self.arr[j][i] for j in range(self.m)] for i in range(self.n)]
        return Matrix(self.m , self.n , ma_tran_chuyen_vi)
    def nhan(self , matrix):
        arr_ket_qua = [[0] * matrix.m for _ in range(self.n)]
        for i in range(self.n):
            for j in range(matrix.m):
                for k in range(self.m):
                    arr_ket_qua[i][j] += self.arr[i][k] * matrix.arr[k][j]
        return Matrix(self.n , matrix.m , arr_ket_qua)
    def __str__(self):
        return "\n".join(" ".join(map(str , x)) for x in self.arr)))
if __name__ == "__main__":
    arr = []
    t = int(input())
    while True:
        try:
            arr.extend(list(map(int , input().split())))
        except:
            break
    i = 0
    for _ in range(t):
        n , m = arr[i + 0] , arr[i + 1]
        if len(arr) - i < n * m: arr.append(0)
        a = []
        i += 2
        for _ in range(n):
            arr_tmp = []
            for _ in range(m):
                arr_tmp.append(arr[i])
                i += 1
            a.append(arr_tmp)
        matrix = Matrix(n , m , a)
        print(matrix.nhan(matrix.ma_tran_chuyen_vi()))