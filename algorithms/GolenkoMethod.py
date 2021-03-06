def _GolenkoMethod(n, p, k, a, c, m, x, s):
    r = []
    for i in range(n):
        if (i == s * p):
            xr = int((10 ** (2 * k)) * ((10 ** k) * (xr ** 2) -
                                        int((10 ** k) * (xr ** 2)))) / 10 ** (2 * k)
        else:
            x = a * x + c - m * int((a * x + c) / m)
            xr = x / m
        r.append(xr)
        s = s + 1
    return r


def GolenkoMethod():
    print('Вы выбрали метод возмущений Голенко.')
    n = int(input('Введите количество генерируемых чисел (n): '))
    p = int(input('Введите период возумщений (p): '))
    k = int(input('Введите число разрядов (k): '))
    a = int(input('Введите множитель (a): '))
    c = int(input('Введите значение приращения (c): '))
    m = int(input('Введите значение модуля (m): '))
    x = int(input('Введите начальное значение (x): '))
    s = int(input('Введите значение итератора (s): '))
    print(_GolenkoMethod(n, p, k, a, c, m, x, s))


if __name__ == "__main__":
    n = 10      # Моделируемые события
    p = 5       # Период возмущений
    k = 2       # Число разрядов
    a = 302     # Множитель
    c = 4965    # Приращение
    m = 42782   # Модуль
    x = 120     # Начальное значение
    s = 1       # Итератор
    print(_GolenkoMethod(n, p, k, a, c, m, x, s))
