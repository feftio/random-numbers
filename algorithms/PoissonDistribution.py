from math import e, factorial as fac


def _PoissonDistribution(p, n):
    sequence, l = [], n * p
    for m in range(n):
        sequence.append(((l ** m) * (e ** (-l))) / fac(m))
    return sequence


def PoissonDistribution():
    pass


if __name__ == '__main__':
    p = 0.08   # Вероятность
    n = 100    # Количесвто событий
    print(_PoissonDistribution(p, n))
