values = {
    c: i
    for (i, c) in enumerate(
        "black brown red orange yellow green blue violet grey white".split()
    )
}
powers = ["", "kilo", "mega", "giga"]


def label(colors):
    numbers = [values[i] for i in colors]
    val = (numbers[0] * 10 + numbers[1]) * 10 ** numbers[2]
    p = 0
    while val != 0 and val % 1000 == 0:
        p += 1
        val //= 1000
    return f"{val} {powers[p]}ohms"
