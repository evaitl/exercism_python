"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.

SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list1, list2):
    def is_sublist(a, b):
        return len(a) <= len(b) and any(a == b[j:j+len(a)] for j in range(len(b) - len(a) + 1))

    match (is_sublist(list1, list2), is_sublist(list2, list1)):
        case (True, True):
            return EQUAL
        case (True, False):
            return SUBLIST
        case (False, True):
            return SUPERLIST
        case (False, False):
            return UNEQUAL
