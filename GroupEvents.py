from LCG import _LCG
from random import random
from tools import prevsum, normalize

def _GroupEvents(p, n):
    if (sum(p) < 0.9999999999999999):
        raise NameError("Сумма вероятностей не равна 1.")
    seq = [random() for _ in range(n)]
    p = prevsum(p)
    k = [0] * (len(p))
    for z in seq:
        for i in range(len(p)):
            if z <= p[i]:
                k[i] += 1
                break
    return k

def GroupEvents():
    print("Вы выбрали линейный конгруэнтный метод.")
    p = [float(v) for v in input('Введите через пробел набор вероятностей наступления событий (p): ').split()]
    n = int(input('Введите количество событий (n): '))
    print(_GroupEvents(p, n))

if __name__ == "__main__":
    p = [0.5, 0.5]   # Набор вероятностей наступления событий
    n = 200          # Количество событий
    print(_GroupEvents(p, n))
