from Golenko import Golenko
from Devis import Devis
from MSM import MSM
from LCG import LCG
from SimpleEvents import SimpleEvents
from GroupEvents import GroupEvents

methods = [Golenko, Devis, MSM, LCG, SimpleEvents, GroupEvents]
while (True):
    try:
        method = int(input('===================================\nВыберите необходимый метод из списка:\n1. Метод возмущений Голенко;\n2. Метод Дэвиса;\n3. Метод середины квадрата;\n4. Линейный конгруэнтный метод.\n5. Моделирование простых событий.\n6. Моделирование группы событий.\n===================================\n'))
        methods[method - 1]()
    except IndexError:
        print("Ошибка! За введенным индексом нет закрепленного метода.")
    except Exception as error:
        print("Ошибка! {}".format(error))