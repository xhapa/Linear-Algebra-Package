class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.dimension = (len(matrix), len(matrix[0]))

    @classmethod
    def from_values(cls, *args, dim_m, dim_n):
        matrix = [[None] * dim_n
                  for i in range(dim_m)]
        index = 0
        for i in range(dim_m):
            for j in range(dim_n):
                matrix[i][j] = args[index]
                index += 1
        return cls(matrix)

    def __repr__(self):
        rp = ""
        for row in self.matrix:
            rp += str(row)+"\n"
        return rp

    def __add__(self, other):
        resul_matrix = [[None] * self.dimension[1]
                        for i in range(self.dimension[0])]
        if self.dimension != other.dimension:
            raise Exception("Invalid operation, dimensions must be A,B in mXn")
        else:
            for i in range(self.dimension[0]):
                for j in range(self.dimension[1]):
                    resul = 0
                    resul = self.matrix[i][j]+other.matrix[i][j]
                    resul_matrix[i][j] = resul

        return Matrix(resul_matrix)

    def __sub__(self, other):
        resul_matrix = [[None] * self.dimension[1]
                        for i in range(self.dimension[0])]
        if self.dimension != other.dimension:
            raise Exception("Invalid operation, dimensions must be A,B in mXn")
        else:
            for i in range(self.dimension[0]):
                for j in range(self.dimension[1]):
                    resul = 0
                    resul = self.matrix[i][j]-other.matrix[i][j]
                    resul_matrix[i][j] = resul

        return Matrix(resul_matrix)

    def scalar_mul(self, scalar):
        if type(scalar) is not int and type(scalar) is not float:
            raise Exception("Invalid argument, must be int or float")

        for i in range(self.dimension[0]):
            for j in range(self.dimension[1]):
                self.matrix[i][j] *= scalar

    def transposed(self):
        resul_matrix = [[None] * self.dimension[0]
                        for i in range(self.dimension[1])]
        for i in range(self.dimension[0]):
            for j in range(self.dimension[1]):
                resul_matrix[j][i] = self.matrix[i][j]

        return Matrix(resul_matrix)

    def is_symmetrical(self):
        return self == self.transposed()

    def is_antisymmetrical(self):
        m = self.transposed()
        m.scalar_mul(-1)
        return self == m

    def __mul__(self, other):
        resul_matrix = [[None] * other.dimension[1]
                        for i in range(self.dimension[0])]
        if self.dimension[1] is not other.dimension[0]:
            raise Exception(
                "Invalid matrix multiplication, dimensions must be mXn * nXp ")
        else:
            for i in range(self.dimension[0]):
                for j in range(other.dimension[1]):
                    resul = 0
                    for k in range(other.dimension[0]):
                        resul += self.matrix[i][k]*other.matrix[k][j]
                    resul_matrix[i][j] = resul

        return Matrix(resul_matrix)

    def __pow__(self, exponent):
        if self.dimension[0] is not len(self.matrix[0]):
            raise Exception(
                "Invalid power of a matrix, dimensions must be nXn")
        else:
            resul_matrix = Matrix(self.matrix)
            for i in range(exponent-1):
                resul_matrix = self*resul_matrix

        return resul_matrix

    def __eq__(self, other):
        equal = True
        if self.dimension == other.dimension:
            for i in range(self.dimension[0]):
                if self.matrix[i] != other.matrix[i]:
                    equal = False
        else:
            equal = False

        return equal
