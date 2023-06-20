from string import ascii_lowercase as lc
from itertools import cycle
from random import choices

_ia=dict([*zip(lc,range(26))])

class Cipher:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = "".join(choices(lc, k=100))

    def encode(self, text):
        k = cycle(self.key)
        return "".join(
            chr((_ia[t]+_ia[next(k)]) % 26 + ord("a"))
            for t in text if t in lc
        )

    def decode(self, text):
        k = cycle(self.key)
        return "".join(
            chr((_ia[t]-_ia[next(k)]) % 26 + ord("a"))
            for t in text if t in lc
        )
