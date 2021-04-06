def _DevisMethod(s, n, m):
    p = len(s) - 1
    for j in range(n):
        t = s[p + j] + s[j]
        if t >= m:
            t -= m
        s.append(t / m)
    return s[p + 1:]


def DevisMethod(cli, name):
    cli.out(f'Вы выбрали [magenta]{name}[/magenta].')
    s = cli.float_list(
        'Введите через пробел миниимум два начальных значения (z0, z1...): ')
    m = cli.int('Введите значение модуля (m): ')
    n = cli.int('Введите количество генерируемых чисел (n): ')
    cli.table(['Число'], _DevisMethod(list(s), n, m), autoheader='z\\[i]',
              autostart=len(s), autoformat='z[{}]')


if __name__ == "__main__":
    s = [0.36, 0.45, 0.62]   # Список начальных значений
    m = 4                    # Значение модуля
    n = 2                    # Количество генерируемых чисел
    print(_DevisMethod(s, n, m))
