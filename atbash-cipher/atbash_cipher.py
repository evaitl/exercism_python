from string import ascii_lowercase, ascii_uppercase
from itertools import zip_longest

TR = str.maketrans(
    ascii_lowercase + ascii_uppercase, ascii_lowercase[::-1] + ascii_lowercase[::-1]
)


def encode(plain_text):
    xlat=''.join(ch for ch in plain_text.translate(TR) if ch.isalnum())
    return " ".join(xlat[i:i+5] for i in range(0,len(xlat),5))


def decode(ciphered_text):
    return "".join(ch for ch in ciphered_text.translate(TR) if ch.isalnum())
