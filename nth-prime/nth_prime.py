from itertools import count, chain


def prime(number):
    if number <= 0:
        raise ValueError("there is no zeroth prime")
    primes = []
    for i in chain((2,), count(3, 2)):
        if all(i % p > 0 for p in primes):
            primes.append(i)
            if len(primes) >= number:
                return primes[number - 1]
