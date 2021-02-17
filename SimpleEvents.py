from random import random

def _SimpleEvents(p, n):
    seq, k = [random() for _ in range(n)], 0
    for z in seq:
        if z < p:
            k += 1
    return k

def SimpleEvents():
    print('Вы выбрали моделирование простых событий.')
    p = float(input('Введите вероятность наступления события (p): '))
    n = int(input('Введите количество событий (n): '))
    print(_SimpleEvents(p, n)) 

if __name__ == "__main__":
    p = 0.2   # Вероятность наступления события
    n = 200   # Количество событий
    print(_SimpleEvents(p, n))