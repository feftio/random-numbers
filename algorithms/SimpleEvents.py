from LCG import _LCG
from math import exp
from random import random

def SimpleEvents(p, event):
    seq = normalize(_LCG(400, 118, 5942, 32777, 200))
    # seq = [random() for _ in range(200)]
    k = 0
    for z in seq:
        if z < p:
            event()
            k += 1
    return k

def sigmoid(x):
    return 1 / (1 + exp(-x))

def normalize(nums):
    MIN, MAX = min(nums), max(nums)
    return [((num - MIN) / (MAX - MIN)) for num in nums]

if __name__ == "__main__":
    a = 400     # Множитель
    z = 118     # Начальное значение
    c = 5942    # Значение приращения
    m = 32777   # Значение модуля
    n = 200     # Количесвто генерируемых чисел
    p = 0.3     # Вероятность наступления события

    k = 0

    def event():
        pass

    print(SimpleEvents(p, event))
