from utils import digits_up, digits_down


def _MSM(number, count):
    sequence = []
    for _ in range(count):
        (number, counter) = digits_up(number) if (
            number > -1 and number < 1) else (number, len(str(number)))
        number = int(number ** 2 %
                     (10 ** (counter + counter // 2)) / (10 ** (counter // 2)))
        sequence.append(digits_down(number)[0])
    return sequence

    # number = int(number % (10 ** 6) / (10 ** 2)) # 4 counter = 7
    # number = int(number % (10 ** 7) / (10 ** 2)) # 5 counter = 9
    # number = int(number % (10 ** 9) / (10 ** 3)) # 6 counter = 11
    # number = int(number % (10 ** 10) / (10 ** 3)) # 7 counter = 13
    # number = int(number % (10 ** 12) / (10 ** 4)) # 8 counter = 15


def MSM(cli, name):
    cli.out(f'Вы выбрали [magenta]{name}[/magenta].')
    number = cli.float('Введите начальное значение (z0): ')
    count = cli.int('Введите количество генерируемых чисел (n): ')
    cli.table(['Число'], _MSM(number, count),
              autoheader='z(i)', autoformat='z({})')


if __name__ == "__main__":
    number = 0.8933   # Начальное значение
    count = 3         # Количество генерируемых чисел
    print(_MSM(number, count))