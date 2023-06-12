# Score categories.
# Change the values as you see fit.
from collections import Counter

YACHT = lambda x: int(len(set(x)) == 1) and 50
ONES = lambda x: Counter(x)[1]
TWOS = lambda x: Counter(x)[2] * 2
THREES = lambda x: Counter(x)[3] * 3
FOURS = lambda x: Counter(x)[4] * 4
FIVES = lambda x: Counter(x)[5] * 5
SIXES = lambda x: Counter(x)[6] * 6
FULL_HOUSE = lambda x: int(sorted(Counter(x).values()) == [2, 3]) and sum(x)
FOUR_OF_A_KIND = lambda x: int(max(Counter(x).values()) >= 4) and 4 * sorted(x)[2]
LITTLE_STRAIGHT = lambda x: int(sorted(x) == [1, 2, 3, 4, 5]) and 30
BIG_STRAIGHT = lambda x: int(sorted(x) == [2, 3, 4, 5, 6]) and 30
CHOICE = lambda x: sum(x)


def score(dice, category):
    return category(dice)
