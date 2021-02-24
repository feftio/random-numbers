from LCG import _LCG
from random import random
from tools import prevsum, normalize

def _GroupEvents(p, n):
    if (sum(p) < 0.9999999999999999):
        raise Exception('Сумма значений вероятностей не равна 1.')
    seq = [random() for _ in range(n)]
    # seq = normalize(_LCG(405, 117, 6925, 32760, 2))
    p = prevsum(p)
    k = [0] * (len(p))
    for z in seq:
        for i in range(len(p)):
            if z <= p[i]:
                k[i] += 1
                break
    return k

def GroupEvents():
    print('Вы выбрали моделирование группы событий.')
    p = [float(v) for v in input('Введите через пробел набор вероятностей наступления событий (p): ').split()]
    n = int(input('Введите количество событий (n): '))
    print(_GroupEvents(p, n)) 

if __name__ == "__main__":
    p = [0.1, 0.2, 0.3, 0.4]   # Набор вероятностей наступления событий
    n = 2                      # Количество событий
    print(_GroupEvents(p, n))