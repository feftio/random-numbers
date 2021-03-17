import sys
sys.path.append('./algorithms')

from random import random
import matplotlib.pyplot as plt
import numpy as np

from utils import fun_max, is_belong_over, is_belong_under


''' Метод исключения Неймана '''


def _NeumannMethod(f, a, b, n):
    M, x, y = f(fun_max(f, a, b)), [], []
    while(len(x) != n):
        z1, z2 = random(), random()
        xp, yp = a + z1 * (b - a), M * z2
        if (yp < M) and (xp > a) and (xp < b) and (yp > 0) and is_belong_under(f, xp, yp):
            x.append(xp)
            y.append(yp)
    return x, y


if __name__ == '__main__':
    a = 1
    b = 5
    n = 100

    exec(open("C:\\Users\\admin\\Desktop\\Projects\\random-numbers\\examples\\function.py").read())

    # def f(x):
    #     return 2 * x + x ** 4

    result = _NeumannMethod(f, a, b, n)
    print(result[0])

    x_fun = np.linspace(a, b, 100)
    plt.plot(x_fun, f(x_fun))
    plt.plot(result[0], result[1], 'o', ms=2)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('_NeumannMethod')
    plt.show()
