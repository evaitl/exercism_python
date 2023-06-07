def abbreviate(words):
    first = True
    acc = []
    for ch in (i for i in words.replace("-", " ") if (i.isalpha() or i.isspace())):
        match (first, ch.isalpha()):
            case (True, True):
                first = False
                acc.append(ch.upper())
            case (False, False):
                first = True

    return "".join(acc)
