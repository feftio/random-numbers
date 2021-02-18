def normalize(nums):
    MIN, MAX = min(nums), max(nums)
    return [((num - MIN) / (MAX - MIN)) for num in nums]

def prevsum(l):
    ln = [0] * (len(l))
    for i in range(len(l)):
        for j in range(i + 1):
            ln[i] += l[j]
    return ln

def freqconvert(m):
    s = sum(m)
    return ([x / s for x in m])