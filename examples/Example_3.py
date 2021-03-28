import sys
from random import random
sys.path.append('./algorithms')


''' Метод обратной функции '''


def _InverseFunctionMethod(f, n):
    sequence = []
    for _ in range(n):
        z = random()
        sequence.append(f(z))
    return sequence


if __name__ == '__main__':
    n = 10      # Количество событий

    def f(x):   # Интегрированная функцияч распределения (Плотность)
        return 1 - (1 - x)

    print(_InverseFunctionMethod(f, n))
