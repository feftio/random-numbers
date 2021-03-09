import sys
from random import random
sys.path.append('./algorithms')

from tools import fun_max, is_belong_over, is_belong_under


''' Метод исключения Неймана '''


# def _NeumannMethod(f, a, b, n):
#     M = f(fun_max(f, a, b))
#     x, y = [], []
#     for i in range(n):
#         z1, z2 = random(), random()
#         x.append(a + z1 * (b - a))
#         y.append(M * z2)

#     return x

def _NeumannMethod(f, a, b, n):
    M = f(fun_max(f, a, b))
    z1, z2 = 0.75, 0.2
    x = a + z1 * (b - a)
    y = M * z2

    return x, y


def NeumannMethod():
    pass


if __name__ == '__main__':
    a = 1
    b = 5
    n = 10

    def f(x):
        return 2 * x + x ** 2

    print(_NeumannMethod(f, a, b, n))
