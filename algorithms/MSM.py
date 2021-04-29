from algorithms.utils import digits_up, digits_down


def _MSM(z, n):
    sequence = []
    for _ in range(n):
        (z, counter) = digits_up(z) if (
            z > -1 and z < 1) else (z, len(str(z)))
        z = int(z ** 2 %
                (10 ** (counter + counter // 2)) / (10 ** (counter // 2)))
        sequence.append(digits_down(z)[0])
    return sequence

    # z = int(z % (10 ** 6) / (10 ** 2)) # 4 counter = 7
    # z = int(z % (10 ** 7) / (10 ** 2)) # 5 counter = 9
    # z = int(z % (10 ** 9) / (10 ** 3)) # 6 counter = 11
    # z = int(z % (10 ** 10) / (10 ** 3)) # 7 counter = 13
    # z = int(z % (10 ** 12) / (10 ** 4)) # 8 counter = 15


def MSM(cli, name):
    z0 = cli.float('Введите начальное значение (z0): ')
    n = cli.int('Введите количество генерируемых чисел (n): ')
    cli.table(['Число'], _MSM(z0, n),
              autoheader='z(i)', autoformat='z({})')


if __name__ == "__main__":
    z0 = 0.8933   # Начальное значение
    n = 3         # Количество генерируемых чисел
    print(_MSM(z0, n))
