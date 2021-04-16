from math import log
from random import random


def _ErlangProcess(lm, k, t):
    sequence, _t = [], 0
    while(_t < t):
        for n in range(k):
            _t += -(1 / lm) * log(random())
        sequence.append(_t)
    return sequence[:len(sequence) - 1]


def ErlangProcess(cli, name):
    cli.out(f'Вы выбрали [magenta]{name}[/magenta].')
    lm = cli.float('Введите интенсивность потока (lm): ')
    t = cli.int('Введите время (t): ')
    k = cli.int('Введите порядок (k): ')
    cli.table(['Время'], _ErlangProcess(lm, k, t),
              autoheader='t(i)', autoformat='t({})')


if __name__ == '__main__':
    lm = 1
    k = 10
    t = 100
    for value in _ErlangProcess(lm, k, t):
        print(value)
