import random
import math


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def inverse_root(n):
    return 1 / math.sqrt(n)

cache = {}
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    def slowfun_inner(x, y):
        tup = (x, y)
        if tup not in cache:
            v = math.pow(x, y)
            v = math.factorial(v)
            v //= (x + y)
            v %= 982451653
            cache[tup] = v
        return cache[tup]
    return slowfun_inner(x,y)



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
