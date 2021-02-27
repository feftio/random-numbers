def _GeometricDist(p, n):
    sequence, q = [], 1 - p
    for i in range(1, n + 1):
        sequence.append(q ** (i - 1) * p)
    return sequence

def GeometricDist():
    pass

if __name__ == '__main__':
    p = 0.5  # Вероятность
    n = 5    # Количество событий
    print(sum(_GeometricDist(p, n)))