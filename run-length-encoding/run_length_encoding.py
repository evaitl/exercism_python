import re

_dp = re.compile(r"(\d+)(.)")


def decode(string):
    return _dp.subn(lambda mo: mo.group(2) * int(mo.group(1)), string)[0]


_ep = re.compile(r"((.)\2+)")


def encode(string):
    return _ep.subn(lambda mo: str(len(mo.group(1))) + mo.group(2), string)[0]
