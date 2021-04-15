from random import random
from algorithms.utils import prevsum


def _GroupEvents(p, n):
    # round(float(Decimal(str(sum(p)))), 2)
    if (round(sum(p), 3) != 1):
        return 'Сумма вероятностей не равна 1.'
    sequence = [random() for _ in range(n)]
    p = prevsum(p)
    frequency = [0] * (len(p))
    for number in sequence:
        for i in range(len(p)):
            if number <= p[i]:
                frequency[i] += 1
                break
    return frequency


def GroupEvents(cli, name):
    cli.out(f'Вы выбрали [magenta]{name}[/magenta].')
    p = cli.float_list(
        'Введите через пробел набор вероятностей событий (p1 p2 ...): ')
    n = cli.int('Введите количество событий (n): ')
    frequency = _GroupEvents(p, n)
    if isinstance(frequency, str):
        cli.out(frequency)
    else:
        headers = [f'Событие {i + 1}' for i in range(len(frequency))]
        cli.table(headers, [frequency])


if __name__ == "__main__":
    p = [0.1, 0.2, 0.3, 0.4]   # Набор вероятностей событий
    n = 10                     # Количество событий
    print(_GroupEvents(p, n))
