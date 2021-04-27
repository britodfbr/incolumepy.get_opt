from random import randint, random
from time import time


def gen_random(op):
    try:
        op = int(op)
        yield {
            1: time(),
            2: random(),
            3: randint(1, 10),
        }.get(op)
    except:
        raise


if __name__ == '__main__':
    a = gen_random(1)
    b = gen_random('2')
    c = gen_random('3')

    print(next(a))
    print(next(b))
    print(next(c))
    for i in range(10):
        print(next(a))