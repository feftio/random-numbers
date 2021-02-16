from LCG import _LCG
from math import exp
from random import random

def SimpleEvents(p):
    # seq = normalize(_LCG(400, 118, 5942, 32777, 200))
    seq = [random() for _ in range(200)]
    k = 0
    for z in seq:
        if z < p:
            k += 1
    return "Событие произошло {} раз из {}.".format(k, len(seq))

def sigmoid(x):
    return 1 / (1 + exp(-x))

def normalize(nums):
    MIN, MAX = min(nums), max(nums)
    return [((num - MIN) / (MAX - MIN)) for num in nums]

if __name__ == "__main__":
    p = 0.3     # Вероятность наступления события
    print(SimpleEvents(p))

