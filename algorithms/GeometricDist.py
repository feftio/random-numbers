def _GeometricDist(p, n):
    s, q = [], 1 - p
    for i in range(1, n + 1):
        s.append(q ** (i - 1) * p)
    return s

def GeometricDist():
    pass

if __name__ == '__main__':
    p = 0.5  # Вероятность
    n = 5    # Количество событий
    print(sum(_GeometricDist(p, n)))