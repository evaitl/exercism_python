from itertools import chain, count


def factors(value):
    f = []
    pg = chain((2,), count(3, 2))
    while value > 1:
        pn = next(pg)
        while value % pn == 0:
            f.append(pn)
            value //= pn
    return f
