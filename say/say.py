ones = lambda x: 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen nineteen'.split()[x]
tens = lambda x: 'zero ten twenty thirty forty fifty sixty seventy eighty ninety'.split()[x]
def say(n):
    if not (0 <= n < 1e12): 
        raise ValueError("input out of range")    
    _ , d, func, txt, hyphen = list(filter(lambda x: x[0],
        [( n <  20,           1, ones, '',           ''),
         ( n < 1e2,          10, tens, '',          '-'),
         ( n < 1e3,         100, ones, ' hundred',  ' '),
         ( n < 1e6,        1000, say, ' thousand', ' '),
         ( n < 1e9,     1000000, say, ' million',  ' '),
         ( n < 1e12, 1000000000, say, ' billion',  ' ')]))[0]
    q, r = divmod(n, d)
    return func(q) + txt + ('' if r==0 else hyphen + say(r))
