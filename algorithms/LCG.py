def _LCG(a, z, c, m, n):
    sequence = [z]
    for _ in range(n):
        number = (a * sequence[len(sequence) - 1] + c) % m
        sequence.append(number)
    return sequence[1:]


def LCG(cli, name):
    cli.out(f'Вы выбрали [magenta]{name}[/magenta].')
    a = cli.int('Введите множитель (a): ')
    z = cli.int('Введите начальное значение (z): ')
    c = cli.int('Введите значение приращения (c): ')
    m = cli.int('Введите значение модуля (m): ')
    n = cli.int('Введите количество генерируемых чисел (n): ')
    cli.table(['Число'], _LCG(a, z, c, m, n), autoheader='Номер')


if __name__ == "__main__":
    a = 7   # Множитель
    z = 7   # Начальное значение
    c = 7   # Значение приращения
    m = 8   # Значение модуля
    n = 3   # Количесвто генерируемых чисел
    print(_LCG(a, z, c, m, n))
