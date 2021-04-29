from math import e, factorial as fac


def _PoissonDistribution(p, n):
    sequence, lmd = [], n * p
    for m in range(n):
        sequence.append(((lmd ** m) * (e ** (-lmd))) / fac(m))
    return sequence


def PoissonDistribution(cli, name):
    p = cli.float('Введите значение вероятности: ')
    n = cli.int('Введите количество событий: ')
    cli.table(['Число'], _PoissonDistribution(p, n),
              autoheader='z(i)', autoformat='z({})')


if __name__ == '__main__':
    p = 0.08   # Вероятность
    n = 100    # Количесвто событий
    print(_PoissonDistribution(p, n))
