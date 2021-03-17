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
        key = list(self.algorithms.keys())[index - 1]
        self.algorithms[key](cli, name=key)

    def cycle(self):
        while True:
            self.all()
            try:
                self.choose()
            except IndexError:
                cli.out('Алгоритма с введенным номером нет в списке.')
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
