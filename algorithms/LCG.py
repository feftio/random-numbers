def _LCG(a, z, c, m, n):
    r = []
    for _ in range(n):
        z = (a * z + c) % m
        r.append(z)
    return r


def LCG():
    print('Вы выбрали линейный конгруэнтный метод.')
    a = int(input('Введите множитель (a): '))
    z = int(input('Введите начальное значение (z): '))
    c = int(input('Введите значение приращения (c): '))
    m = int(input('Введите значение модуля (m): '))
    n = int(input('Введите количество генерируемых чисел (n): '))
    print(_LCG(a, z, c, m, n))


if __name__ == "__main__":
    a = 7   # Множитель
    z = 8   # Начальное значение
    c = 8   # Значение приращения
    m = 9   # Значение модуля
    n = 4   # Количесвто генерируемых чисел
    print(_LCG(a, z, c, m, n))
