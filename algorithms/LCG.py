def _LCG(a, z, c, m, n):
    sequence = [z]
    for _ in range(n):
        number = (a * sequence[len(sequence) - 1] + c) % m
        sequence.append(number)
    return sequence[1:]


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
    n = 3   # Количесвто генерируемых чисел
    print(_LCG(a, z, c, m, n))