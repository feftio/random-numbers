from random import random


def _ComplexEvent(p1, p2, n):
    k = [0] * 4
    for j in range(n):
        z1, z2 = random(), random()
        if z1 <= p1 and z2 <= p2:
            k[0] += 1
            continue
        if not(z1 <= p1) and not(z2 <= p2):
            k[1] += 1
            continue
        if z1 <= p1 and not(z2 <= p2):
            k[2] += 1
            continue
        if not(z1 <= p1) and z2 <= p2:
            k[3] += 1
            continue
    return k


def ComplexEvents(cli, name):
    p = cli.float_list(
        'Введите два значения вероятности событий через пробел (p1, p2): ')
    n = cli.int('Введите количество событий (n): ')
    cli.table(['AB', '!AB', 'A!B', '!A!B'], [_ComplexEvent(p[0], p[1], n)])


if __name__ == '__main__':
    p1, p2 = 0.15, 0.2   # Вероятности
    n = 1000             # Число испытаний
    print(_ComplexEvent(p1, p2, n))
