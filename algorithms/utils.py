from decimal import Decimal
# from scipy import optimize as opt


def normalize(numbers):
    MIN, MAX = min(numbers), max(numbers)
    return [((number - MIN) / (MAX - MIN)) for number in numbers]


def prevsum(probs):
    _probs = [0] * (len(probs))
    for i in range(len(probs)):
        for j in range(i + 1):
            _probs[i] += probs[j]
    return _probs


def freqconvert(probs):
    _sum = sum(probs)
    return ([prob / _sum for prob in probs])


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


# def fun_max(f, a, b):
#     return round(opt.fminbound(lambda x: -f(x), a, b))


def is_belong_over(f, x, y):
    y_default = f(x)
    if y <= y_default:
        return False
    return True


def is_belong_under(f, x, y):
    y_default = f(x)
    if y >= y_default:
        return False
    return True


def is_belong(f, x, y):
    y_default = f(x)
    if y == y_default:
        return False
    return True
