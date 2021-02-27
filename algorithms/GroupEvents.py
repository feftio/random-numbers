from LCG import _LCG
from random import random
from tools import prevsum, normalize, freqconvert
from decimal import Decimal


def _GroupEvents(probs, count):
    if (Decimal(str(sum(probs))) != 1):
        raise Exception('Сумма значений вероятностей не равна 1.')
    sequence = [random() for _ in range(count)]
    probs = prevsum(probs)
    frequency = [0] * (len(probs))
    for number in sequence:
        for i in range(len(probs)):
            if number <= probs[i]:
                frequency[i] += 1
                break
    return frequency


def GroupEvents():
    print('Вы выбрали моделирование группы событий.')
    probs = [float(prob) for prob in input(
        'Введите через пробел набор вероятностей событий (probs): ').split()]
    count = int(input('Введите количество событий (count): '))
    print(_GroupEvents(probs, count))


if __name__ == "__main__":
    probs = [0.1, 0.2, 0.3, 0.4]   # Набор вероятностей событий
    count = 10                     # Количество событий
    print(_GroupEvents(probs, count))
