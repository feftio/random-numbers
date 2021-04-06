def _GeometricDistribution(p, n):
    sequence, q = [], 1 - p
    for i in range(1, n + 1):
        sequence.append(float("{0:.16f}".format(q ** (i - 1) * p)))
    return sequence


def GeometricDistribution(cli, name):
    cli.out(f'Вы выбрали [magenta]{name}[/magenta].')
    p = cli.float('Введите значение вероятности: ')
    n = cli.int('Введите количество событий: ')
    cli.table(['Число'], _GeometricDistribution(p, n),
              autoheader='z(i)', autoformat='z({})')


if __name__ == '__main__':
    p = 0.23  # Вероятность
    n = 10    # Количество событий
    print(_GeometricDistribution(p, n))
