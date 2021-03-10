from math import e, factorial as fac


def _PoissonDistribution(p, n):
    sequence, lmd = [], n * p
    for m in range(n):
        sequence.append(((lmd ** m) * (e ** (-lmd))) / fac(m))
    return sequence


def PoissonDistribution(io):
    io.out()


if __name__ == '__main__':
    p = 0.08   # Вероятность
    n = 100    # Количесвто событий
    print(_PoissonDistribution(p, n))
