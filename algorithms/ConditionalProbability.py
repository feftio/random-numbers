from random import random


def _ConditionalProbability(pa, pb, pba, n=10):
    frequencies, pb_a = [0] * 4, (pb - pa * pba) / (1 - pa)
    for i in range(n):
        z1, z2 = random(), random()
        if z1[i] < pa:
            if z2[i] < pba:
                frequencies[0] += 1
            else:
                frequencies[1] += 1
        else:
            if z2[i] < pb_a:
                frequencies[2] += 1
            else:
                frequencies[3] += 1
    return frequencies


def ConditionalProbability(cli, name):
    pass


if __name__ == '__main__':
    pa = 0.5
    pb = 0.6
    pba = 0.8
    n = 10
    print(_ConditionalProbability(pa, pb, pba, n))
