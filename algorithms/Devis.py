def _Devis(s, n, m):
    p = len(s) - 1
    for j in range(n):
        t = s[p + j] + s[j]
        if t >= m:
            t -= m
        s.append(t / m)
    return s[p + 1:]

def Devis():
    print('Вы выбрали метод Дэвиса.')
    s = [float(v) for v in input('Введите через пробел миниимум два начальных значения (s): ').split()]
    n = int(input('Введите количество генерируемых чисел (n): '))
    m = int(input('Введите значение модуля (m): '))
    print(_Devis(s, n, m))

if __name__ == "__main__":
    s = [0.36, 0.45, 0.62]   # Список начальных значений
    n = 10                   # Количество генерируемых чисел
    m = 4                    # Значение модуля
    print(_Devis(s, n, m))