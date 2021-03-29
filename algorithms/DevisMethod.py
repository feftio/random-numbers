def _DevisMethod(s, n, m) -> list:
    p = len(s) - 1
    for j in range(n):
        t = s[p + j] + s[j]
        if t >= m:
            t -= m
        s.append(t / m)
    return s[p + 1:]


def DevisMethod(cli, name):
    s = cli.float_list(
        'Введите через пробел миниимум два начальных значения (s): ')
    n = cli.int('Введите количество генерируемых чисел (n): ')
    m = cli.int('Введите значение модуля (m): ')
    cli.table(['Число'], _DevisMethod(s, n, m), autoheader='Номер')


if __name__ == "__main__":
    s = [0.36, 0.45, 0.62]   # Список начальных значений
    n = 2                    # Количество генерируемых чисел
    m = 4                    # Значение модуля
    print(_DevisMethod(s, n, m))
