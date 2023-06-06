def is_valid(isbn):
    isbn = isbn.replace("-", "").strip()
    if len(isbn) != 10 or not set(isbn) <= set("0123456789X"):
        return False
    if isbn.find("X") not in [-1, 9]:
        return False

    def toint(chr):
        if chr.isdigit():
            return int(chr)
        return 10

    return (
        sum(toint(x) * y for x, y in zip(isbn.replace("-", ""), range(10, 0, -1))) % 11
        == 0
    )
