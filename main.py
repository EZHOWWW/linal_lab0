from matrix import Matrix, SquareMatrix
from decimal import Decimal


def get_matrix():
    inp = input('write size').split(' ')
    size = int(inp[0]), int(inp[1])
    mtrx = []
    for i in range(size[0]):
        mtrx.append([Decimal(i) for i in input().split(' ')])
    return mtrx


def task1():
    mtrx = SquareMatrix(get_matrix())
    print(f'trace: {mtrx.get_trace()}')
    print(f'el: 1, 1: {mtrx[(1, 1)]}')


def task2():
    mtrx1 = Matrix(get_matrix())
    mtrx2 = Matrix(get_matrix())
    print(f'sum:\n{(mtrx1+mtrx2).mtrx}')


def task3():
    mtrx = SquareMatrix(get_matrix())
    det = mtrx.det()
    print('нет' if det == 0 else 'да')


def main():
    task3()


if __name__ == '__main__':
    main()
