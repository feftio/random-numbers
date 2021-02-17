def _MSM(v, n):
    r, v = [], v * 111
    for i in range(n):
        s = str(v ** 2)
        bl = len(s) // 4
        br = bl + 1 if len(s) % 2 else bl
        v = int(s[bl : -br])
        r.append(v)
    return r

def MSM():
    print('Вы выбрали метод середины квадрата.')
    v = int(input('Введите начальное значение (v): '))
    n = int(input('Введите количество генерируемых чисел (n): '))
    print(_MSM(v, n))

if __name__ == "__main__":
    v = 3124   # Начальное значение
    n = 40     # Количество генерируемых чисел
    print(_MSM(v, n))