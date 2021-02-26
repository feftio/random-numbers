from decimal import Decimal


def normalize(numbers):
    MIN, MAX = min(numbers), max(numbers)
    return [((number - MIN) / (MAX - MIN)) for number in numbers]


def prevsum(l):
    ln = [0] * (len(l))
    for i in range(len(l)):
        for j in range(i + 1):
            ln[i] += l[j]
    return ln


def freqconvert(m):
    s = sum(m)
    return ([x / s for x in m])


def digits_up(number):
    if number <= -1 or number >= 1:
        return (number, 0)
    counter = 0
    while(round(number) != number):
        number, counter = Decimal(str(number)) * 10, counter + 1
    number = int(number)
    return number, counter


def digits_down(number):
    if number > -1 and number < 1:
        return (number, 0)
    number, counter = int(number), 0
    while((number >= 1) or (number <= -1)):
        number, counter = Decimal(str(number)) / 10, counter + 1
    number = float(number)
    return number, counter


if __name__ == '__main__':
    print(digits_up(0.33432))
