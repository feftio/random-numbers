from cli import cli
from rich import box


class Printer:

    def __init__(self, algorithms):
        self.algorithms = algorithms

    def all(self):
        cli.table(['Название'], list(
            self.algorithms.keys()), autoheader='Номер')

    def choose(self):
        index = cli.int('Введите [magenta]номер[/magenta] алгоритма: ') - 1
        return list(self.algorithms.values())[index](cli, list(self.algorithms.keys())[index])

    def cycle(self):
        while True:
            self.all()
            self.choose()
            cli.wait()


if __name__ == '__main__':
    pass

# algorithms = [Golenko, Devis, MSM, LCG, SimpleEvents, GroupEvents]
# while (True):
#     try:
#         algorithm = int(input('=====================================\nВыберите необходимый алгоритм из списка:\n1. Метод возмущений Голенко;\n2. Метод Дэвиса;\n3. Метод середины квадрата;\n4. Линейный конгруэнтный метод;\n5. Моделирование простых событий;\n6. Моделирование группы событий.\n=====================================\n'))
#         algorithms[algorithm - 1]()
#     except IndexError:
#         print('Ошибка! За введенным индексом нет закрепленного метода.')
#     except Exception as error:
#         print(f'Ошибка! {error}')
