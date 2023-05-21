import math

def standard(i, o, k):
    i = (i + k * math.sin(o)) % (2 * math.pi)
    o = (o + i) % (2 * math.pi)
    return i, o

def rng(i, o, n, k=0.971635, exp=4):
    numbers = []
    try:
        if k <= 0:
            raise ValueError("Value k must be greater than 0")
        if i==0 and o==0:
            raise ValueError("Value i and o cannot both be 0")
        if i < 0 or i >= 2 * math.pi:
            raise ValueError("Value i must be between 0 and 2pi")
        if o < 0 or o >= 2 * math.pi:
            raise ValueError("Value o must be between 0 and 2pi")
        for _ in range(math.ceil(n / 2)):
            i, o = standard(i, o, k)
            num1 = int((i % 1) * (10 ** exp))
            num2 = int((o % 1) * (10 ** exp))
            numbers.append(num1)
            numbers.append(num2)
    except Exception as e:
        print(e)
    return numbers[:n]

i = 0.1
o = 1.0

numbers = rng(i, o, 100, exp=3)
list(map(print,numbers))