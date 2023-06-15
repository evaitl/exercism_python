gifts = [
    "Shouldn't be here",
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, ",
]

ordinals = (
    "zeroeth?",
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
)


def _verse(day):
    ret = f"On the {ordinals[day]} day of Christmas my true love gave to me: "
    if day == 1:
        ret += gifts[1]
    else:
        ret += "".join(gifts[day:1:-1] + ["and ", gifts[1]])
    return ret


def recite(start_verse, end_verse):
    return [_verse(i) for i in range(start_verse, end_verse + 1)]
