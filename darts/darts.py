"""Darts exercism exercise
"""


def score(x, y):
    """Score a dart based on cartesion coords

    :param x: float -
    :param y: float -
    :return: int value
    """
    r2 = x**2 + y**2
    if r2 > 100:
        return 0
    if r2 > 25:
        return 1
    if r2 > 1:
        return 5
    return 10
