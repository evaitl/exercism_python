def roman(number):
    if number < 1 or number >= 4000:
        raise ValueError(f"{number} out of range")
    xlat = (
        (1000, [""] + "M MM MMM".split()),
        (100, [""] + "C CC CCC CD D DC DCC DCCC CM".split()),
        (10, [""] + "X XX XXX XL L LX LXX LXXX XC".split()),
        (1, [""] + "I II III IV V VI VII VIII IX".split()),
    )
    rn = []
    for n, s in xlat:
        i, number = divmod(number, n)
        rn.append(s[i])
    return "".join(rn)
