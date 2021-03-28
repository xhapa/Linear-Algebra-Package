from matrix import Matrix


class Vector(Matrix):
    def __init__(self, vector):
        super().__init__([vector])
        self.magnitude = self.find_magnitude()
        self.direction = None

    def find_magnitude(self):
        resul = 0
        for i in self.matrix[0]:
            resul += i**2
        return resul**(0.5)

    def scalar_product(self, other):
        return int((self * other.transposed()).matrix[0][0])

    @classmethod
    def from_matrix(cls, vector):
        return cls(vector.matrix[0])