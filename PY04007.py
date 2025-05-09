class Matrix:
    def __init__(self, n, m, arr):
        self.n = n
        self.m = m
        self.arr = arr

    def ma_tran_chuyen_vi(self):
        arr_chuyen_vi = [[self.arr[j][i] for j in range(self.n)] for i in range(self.m)]
        return Matrix(self.m, self.n, arr_chuyen_vi)

    def nhan(self, matrix):
        arr_ket_qua = [[0] * matrix.m for _ in range(self.n)]
        for i in range(self.n):
            for j in range(matrix.m):
                for k in range(self.m):
                    arr_ket_qua[i][j] += self.arr[i][k] * matrix.arr[k][j]
        return Matrix(self.n, matrix.m, arr_ket_qua)
    def __str__ (self):
        return "\n".join(" ".join(map(str ,x)) for x in self.arr)

if __name__ == "__main__":
    for _ in range(int(input())):
        n , m = list(map(int , input().split()))
        arr = []
        for _ in range(n):
            arr.append(list(map(int , input().split())))
        matrix = Matrix(n , m , arr)
        print(matrix.nhan(matrix.ma_tran_chuyen_vi()))