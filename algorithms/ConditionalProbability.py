from random import random


def _ConditionalProbability(pa, pba, pb_a, n):
    frequency = [0] * 4
    for _ in range(n):
        z1, z2 = random(), random()
        if z1 < pa:
            if z2 < pba:
                frequency[0] += 1
            else:
                frequency[1] += 1
        else:
            if z2 < pb_a:
                frequency[2] += 1
            else:
                frequency[3] += 1
    return frequency


def ConditionalProbability(cli, name):
    cli.out(f'Вы выбрали [magenta]{name}[/magenta].')
    pa = cli.float('Введите значение вероятности A (pa): ')
    pba = cli.float(
        'Введите значение вероятности B, если событие A произойдет (pba): ')
    pb_a = cli.float(
        'Введите значение вероятности B, если событие A не произойдет (pb_a): ')
    n = cli.int('Введите количество событий: ')
    cli.table(['AB', 'A!B', '!A!B', '!AB'], [
              _ConditionalProbability(pa, pba, pb_a, n)])


if __name__ == '__main__':
    pa = 0.6
    pba = 0.5
    pb_a = 0.75
    n = 10000
    print(_ConditionalProbability(pa, pba, pb_a, n))
