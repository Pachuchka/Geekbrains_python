from random import randint as rnd
class Matrix:
    def __init__(self, m,n):
        self.m = m
        self.n = n
        self.matrix = [[rnd(1,10) for j in range(m)] for i in range(n)]

        #print(self.matrix)
    def __str__(self):
        i=0
        _matrix_str = ""
        while i < self.n:
            _matrix_str = _matrix_str + (str((self.matrix[i]) )+ '\n' )
            i=i+1
        self.str_matrix = _matrix_str
        return f' {self.str_matrix}'

    def __add__(self, other):

        Res_matrix_Sum = Matrix(self.m,self.n)
        i=0
        j = 0
        while i<self.n:

            while j<self.m:
                Res_matrix_Sum.matrix[i][j]=self.matrix[i][j] + other.matrix[i][j]
                j=j+1
            i=i+1
            j = 0
        return Res_matrix_Sum

B = Matrix(3,2)

C = Matrix(3,2)
print(B)
print(C)
print(B+C)