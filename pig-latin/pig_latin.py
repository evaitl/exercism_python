import re

RE = re.compile("^(?P<prefix>x(?!r)|y(?!t)|[^aeiouqxy]*(?:qu?)?)(?P<body>.+)$")


def translate(phrase):
    return " ".join(map(translate_word, phrase.split()))


def translate_word(word):
    gd=RE.match(word).groupdict()
    return f"{gd['body']}{gd['prefix']}ay"
