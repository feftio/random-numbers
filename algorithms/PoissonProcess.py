from random import random
from math import log


def _PoissonProcess(lm, n):
    sequence = [0]
    for i in range(n):
        z = random()
        x = sequence[i] + -(1 / lm) * log(z)
        if x > n:
            break
        sequence.append(x)
    return sequence[1:]


def PoissonProcess(cli, name):
    lm = cli.float('Введите интенсивность потока (lm): ')
    n = cli.int('Введите время (t): ')
    cli.table(['Время'], _PoissonProcess(lm, n),
              autoheader='t(i)', autoformat='t({})')


if __name__ == '__main__':
    lm = 8/24   # Интенсивность потока
    n = 100     # Время
    print(_PoissonProcess(lm, n))
