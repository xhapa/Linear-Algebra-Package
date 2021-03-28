from matrix import Matrix
from vector import Vector


def test():
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [6, 7, 8]])
    m2 = Matrix([[1, 2, 3], [2, 3, 4], [5, 6, 7], [8, 9, 10]])
    m4 = Matrix([[1, 2, 3], [2, 3, 4], [5, 6, 7], [8, 9, 10]])
    m5 = Matrix([[0, -3, 4], [3, 0, 0], [-4, 0, 0]])
    v1 = Vector([1, 5, 6])
    v2 = Vector([2, 2, 0])

    print(m1)
    print(m2)
    m3 = m2*m1
    print(m3)
    print(m1**2)
    m1.scalar_mul(2)
    print(m1)
    print(m2 == m4)
    print(m1+m1)
    print(m5.transposed())
    print(m4.is_symmetrical())
    print(m4.is_antisymmetrical())

    m6 = Matrix.from_values(1, 2, 3, 4, 5, 6, dim_m=2, dim_n=3)
    print(m6)

    print(v1)
    print(v1.magnitude)
    print(v1.dimension)
    print(v1.scalar_product(v2))

    v3 = Vector.from_matrix(v1-v2)
    print(v3)


def main():
    test()
    

if __name__ == '__main__':
    main()
