
class Matrix:

    def __init__(self, matrix : list):
        self.__matrix_list = matrix
        self.__m = len(matrix)
        self.__n = len(matrix[0])


    def __str__(self):
        matrix = ''
        for row in (self.__matrix_list):
            matrix += str(row)+'\n'
        return matrix

    def __matrice_completion(self, num_row, num_column):

        if self.__n < num_column:
            for row in self.__matrix_list:
                row.extend([0] * (num_column - self.__n))
            self.__n = num_column

        if self.__m < num_row:
            self.__matrix_list.extend([[0] * self.__n] * (num_row - self.__m))


    def mult_by_number(self, num):
        for j in range(self.__m):
            for i in range(self.__n):
                self.__matrix_list[j][i] *= num
        return self


    def add_matrix(self, matrix):
        m = max(self.__m, matrix.__m)
        n = max(self.__n, matrix.__n)
        self.__matrice_completion(m, n)
        matrix.__matrice_completion(m, n)
        result = []

        for j in range(m):
            row = []
            for i in range(n):
                el = self.__matrix_list[j][i] + matrix.__matrix_list[j][i]
                row.append(el)
            result.append(row)

        return Matrix(result)


    def subtract_matrix(self, matrix):
        m = max(self.__m, matrix.__m)
        n = max(self.__n, matrix.__n)
        self.__matrice_completion(m, n)
        matrix.__matrice_completion(m, n)
        result = []

        for j in range(m):
            row = []
            for i in range(n):
                el = self.__matrix_list[j][i] - matrix.__matrix_list[j][i]
                row.append(el)
            result.append(row)

        return Matrix(result)


    def transpose(self):
        result = [[0] * self.__m for _ in range(self.__n)]

        for i in range(self.__m):
            result
            for j in range(self.__n):
                result[j][i] = self.__matrix_list[i][j]
        self.__matrix_list = result
        self.__m, self.__n = self.__n, self.__m
        return self



    def mult_by_matrix(self, matrix):
        # if self.__m != matrix.__n:
        #   raise Exception('sfsdfsdfsdf')
        if not self:
            pass

        else:
            result = [[0] * self.__m for _ in range(matrix.__n)]

            for i in range(self.__m):
                for j in range(matrix.__n):
                    for k in range(matrix.__m):
                        result[i][j] += self.__matrix_list[i][k] * matrix.__matrix_list[k][j]
                    
        return Matrix(result)



# A = Matrix([[3, 2],
#             [2, 1],
#             [8, -1]])
# B = Matrix([[1]])
#
# print('Adding two matrices.')
# C = A.add_matrix(B)
# print(C)
#
# print("Subtract matrices.")
# A = Matrix([[1, 2],
#            [3, -6],
#            [2, 0]])
#
# B = Matrix([[2, -6, 8],
#             [3, 0, 5]])
# C = A.subtract_matrix(B)
# print(C)
#
#
# n = 4
# A = Matrix([[3, 2],
#             [2, 1],
#             [8, -1]])
# print(f'Multiplying by number {n}.')
# A.mult_by_number(n)
# print(A)
#
# print(('Transpose matrice.'))
# A = Matrix([[5, 0],
#             [-3, 2],
#             [7, -1]])
# A.transpose()
# print(A)
print('*******************')
print(f'Multiplying by matrice.')
D = Matrix([[4, -2],
            [5, 1],
            [3, 0]])

C = Matrix([[3, 5, 0],
           [4, -2, 1]])

DC = D.mult_by_matrix(C)
print(DC)

CD = C.mult_by_matrix(D)
print(CD)

# Multiply Two Matrices
# 3x3 matrix
# X = Matrix([[12, 7, 3],
#             [4, 5, 6],
#             [7, 8, 9]])
# # 3x4 matrix
# Y = Matrix([[5, 8, 1, 2],
#             [6, 7, 3, 0],
#             [4, 5, 9, 1]])
#
#
# Z = X.mult_by_matrix(Y)
# print(Z)



