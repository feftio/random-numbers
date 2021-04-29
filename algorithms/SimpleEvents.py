from random import random


def _SimpleEvents(p, n):
    seq, k = [random() for _ in range(n)], 0
    for z in seq:
        if z < p:
            k += 1
    return k


def SimpleEvents(cli, name):
    p = cli.float('Введите вероятность наступления события (p): ')
    n = cli.int('Введите количество событий (n): ')
    cli.out(_SimpleEvents(p, n))


if __name__ == "__main__":
    p = 0.2   # Вероятность наступления события
    n = 200   # Количество событий
    print(_SimpleEvents(p, n))
