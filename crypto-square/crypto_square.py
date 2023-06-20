from math import ceil, sqrt


def cipher_text(plain_text):
    pt = "".join(c for c in plain_text.lower() if c.isalnum())
    if not pt:
        return ""
    c = ceil(sqrt(len(pt)))
    r = ceil(len(pt) / c)
    pt += " " * ((c * r) - len(pt))

    return " ".join(pt[i::c] for i in range(c))
