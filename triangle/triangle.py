def tri(f):
    """Triangle function decorator

    PEP-318
    """

    def inner(s):
        s.sort()
        return s[0] + s[1] > s[2] and f(s)

    return inner


@tri
def equilateral(s):
    return s[0] == s[2]


@tri
def isosceles(s):
    return s[0] == s[1] or s[1] == s[2]


@tri
def scalene(s):
    return s[0] != s[1] and s[1] != s[2]
