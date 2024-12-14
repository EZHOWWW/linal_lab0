from decimal import Decimal


class Matrix:
    def __init__(self, mtrx: list[list[Decimal | float | int]] = [[]], size=None):
        for i in range(len(mtrx) - 1):
            if len(mtrx[i]) != len(mtrx[i+1]):
                raise Exception()
        if size is None:
            if mtrx == [[]]:
                self.size = (0, 0)
            else:
                self.size = (len(mtrx), len(mtrx[0]))
        else:
            self.size = size
        self.mtrx: dict[(int, int), Decimal] = {(m, n): Decimal(mtrx[m][n]) for m in range(
            len(mtrx)) for n in range(len(mtrx[m])) if mtrx[m][n] != 0}

    def __getitem__(self, key: tuple[int] | list[int]):
        return self._get((key[0]-1, key[1]-1))

    def _get(self, key: tuple[int] | list[int]):
        return self.mtrx.get(key, Decimal(0))

    def _set(self, key: tuple[int] | list[int], value: Decimal):
        if value == 0:
            self.mtrx.pop(key)
        else:
            self.mtrx[key] = value

    def __setitem__(self, key: tuple[int] | list[int], value: Decimal):
        self._set((key[0]-1, key[1]-1), value)

    def __add__(self, other):
        if self.size != other.size:
            raise Exception()
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if (i, j) in self.mtrx and (i, j) in other.mtrx:
                    self.mtrx[(i, j)] += other.mtrx[(i, j)]
        return self

    def __mul__(self, val: int):
        if type(val) is int:
            return self._mul_int(val)
        elif type(val) is Matrix:
            return self._mul_mat(val)
        else:
            return None

    def _mul_int(self, val: int):
        for i in self.mtrx:
            self.mtrx[i] *= val
        return self

    def _mul_mat(self, mat):
        if self.size[1] != mat.size[0]:
            raise Exception()
        res = Matrix(size=(self.size[0], self.size[1]))
        for i in range(res.size[0]):
            for j in range(res.size[1]):
                res._set((i, j), sum([self._get((i, k)) * mat._get((j, k))
                                      for k in range(self.size[1])]))
        return res

    def __eq__(self, other):
        return self.mtrx == other.mtrx


class SquareMatrix(Matrix):
    def __init__(self, mtrx: list[list[Decimal | float | int]]):
        super().__init__(mtrx)
        for i in range(len(mtrx)-1):
            if len(mtrx[i]) != len(mtrx):
                raise Exception()

    def get_trace(self):
        # След матрицы
        return sum([self._get((i, i)) for i in range(self.size[0])])
