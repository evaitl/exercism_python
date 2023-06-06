def sum_of_multiples(limit, multiples):
    return sum({i for n in multiples if n for i in range(n, limit, n)})
