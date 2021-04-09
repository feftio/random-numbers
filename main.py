from algorithms.ComplexEvents import ComplexEvents
from algorithms.ConditionalProbability import ConditionalProbability
from algorithms.DevisMethod import DevisMethod
from algorithms.GeometricDistribution import GeometricDistribution
# from algorithms.GolenkoMethod import GolenkoMethod
from algorithms.GroupEvents import GroupEvents
from algorithms.LCG import LCG
from algorithms.MSM import MSM
from algorithms.PoissonDistribution import PoissonDistribution
from algorithms.PoissonProcess import PoissonProcess
from algorithms.SimpleEvents import SimpleEvents

from printer import Printer

algorithms = {
    'Сложные события': ComplexEvents,
    'Условная вероятность': ConditionalProbability,
    'Метод Дэвиса': DevisMethod,
    'Геометрическое распределение': GeometricDistribution,
    # 'Метод возмущений Голенко': GolenkoMethod,
    'Групповые события': GroupEvents,
    'Линейный конгруэнтный метод': LCG,
    'Метод середины квадрата': MSM,
    'Распределение Пуассона': PoissonDistribution,
    'Простейший поток': PoissonProcess,
    'Простые события': SimpleEvents
}

printer = Printer(algorithms)
printer.cycle()
