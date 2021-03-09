import sys
sys.path.append('algorithms')

from algorithms.GolenkoMethod import GolenkoMethod
from algorithms.DevisMethod import DevisMethod
from algorithms.MSM import MSM
from algorithms.LCG import LCG
from algorithms.SimpleEvents import SimpleEvents
from algorithms.GroupEvents import GroupEvents
from algorithms.ComplexEvents import ComplexEvents

from printer import Printer

algorithms = {
    'Метод возмущений Голенко': GolenkoMethod,
    'Метод Дэвиса': DevisMethod,
    'Метод середины квадрата': MSM,
    'Линейный конгруэнтный метод': LCG,
    'Моделирование простых событий': SimpleEvents,
    'Моделирование групповых событий': GroupEvents
}

rp = Printer(algorithms)
rp.cycle()

