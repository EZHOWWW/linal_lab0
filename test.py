from matrix import Matrix, SquareMatrix
import unittest as ut


class TestMatrix(ut.TestCase):
    def test_init(self):
        self.assertEqual(Matrix([[1, 0], [0, 4]]).size, (2, 2))
        self.assertEqual(len(Matrix([[1, 0], [0, 4]]).mtrx), 2)
        self.assertEqual(Matrix([[]]).size, (0, 0))
        self.assertEqual(Matrix([[1]]).size, (1, 1))


class TestSquareMatrix(ut.TestCase):
    def test_get_trace(self):
        self.assertEqual(SquareMatrix([[0, 1], [1, 0]]).get_trace(), 0)
        self.assertEqual(SquareMatrix(
            [[1000, 1], [0, 1000]]).get_trace(), 2000)

    def test_sum(self):
        self.assertEqual(
            (Matrix([[1, 2, 3],
                    [4, 5, 6]]) +
             Matrix([[6, 5, 4],
                    [3, 2, 1]])).mtrx,
            Matrix([[7]*3, [7]*3]).mtrx
        )

    def test_mul_int(self):
        self.assertEqual(Matrix([[1, 2, 3], [-1, 2, -3]])
                         * 3, Matrix([[3, 6, 9], [-3, 6, -9]]))

    def test_mul_int(self):
        self.assertEqual(Matrix([[2, 4], [6, 8]]) *
                         Matrix([[1, 0], [0, 1]]), Matrix([[2, 4], [6, 8]]))

    def test_get_minor(self):
        a = SquareMatrix([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]]).get_minor((0, 0))

        self.assertEqual(
            SquareMatrix([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]]).get_minor((0, 0)),
            SquareMatrix([[5, 6], [8, 9]])
        )

    def test_get_det(self):
        self.assertEqual(
            SquareMatrix([[1, 0, 0],
                          [0, 1, 0],
                         [0, 0, 1]]).det(), 1
        )


if __name__ == '__main__':
    ut.main()
