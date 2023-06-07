from string import ascii_uppercase, ascii_lowercase


def rotate(text, key):
    newchars = ascii_lowercase[key:] + ascii_lowercase[:key]
    tr = str.maketrans(ascii_lowercase + ascii_uppercase, newchars + newchars.upper())
    return text.translate(tr)
