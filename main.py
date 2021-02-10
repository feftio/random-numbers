from algorithms.Golenko import Golenko
from algorithms.Devis import Devis
from algorithms.MSM import MSM
from algorithms.LCG import LCG

methods = [Golenko, Devis, MSM, LCG]
while (True):
    method = int(input('Выберите необходимый метод из списка:\n1. Метод возмущений Голенко;\n2. Метод Дэвиса;\n3. Метод середины квадрата;\n4. Линейный конгруэнтный метод.\n'))
    try:
        methods[method - 1]()
    except IndexError:
        print("За введенным индексом нет закрепленного метода.")