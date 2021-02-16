from LCG import _LCG
from random import random

def normalize(nums):
    MIN, MAX = min(nums), max(nums)
    return [((num - MIN) / (MAX - MIN)) for num in nums]

def prevsum(l):
    ln = [0] * (len(l) - 1)
    for i in range(len(l) - 1):
        for j in range(i + 1):
            ln[i] += l[j]
    return ln

def GroupEvent(p):
    if (sum(p) != 1):
        raise NameError("Сумма вероятностей не равна 1.")
    seq = normalize(_LCG(400, 118, 5942, 32777, 200))
    # seq = [random() for _ in range(200)]
    p = prevsum(p)
    k = [0] * (len(p) + 1) # To do...
    for z in seq:
        for i in range(len(p)):
            if z < p[i]:
                k[i] += 1
                break




if __name__ == "__main__":
    p = [0.3, 0.2, 0.3, 0.2]   # Набор вероятностей наступления событий

    print(GroupEvent(p))
