from Golenko import Golenko
from Devis import Devis
from MSM import MSM
from LCG import LCG
from SimpleEvents import SimpleEvents
from GroupEvents import GroupEvents

methods = [Golenko, Devis, MSM, LCG, SimpleEvents, GroupEvents]
while (True):
    method = int(input('Выберите необходимый метод из списка:\n1. Метод возмущений Голенко;\n2. Метод Дэвиса;\n3. Метод середины квадрата;\n4. Линейный конгруэнтный метод.\n5. Моделирование простых событий.\n6. Моделирование групповых событий.\n'))
    try:
        methods[method - 1]()
    except IndexError:
        print("За введенным индексом нет закрепленного метода.")