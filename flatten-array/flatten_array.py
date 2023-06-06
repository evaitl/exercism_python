def flatten(iterable):
    f = []
    for i in iterable:
        if isinstance(i, list):
            f.extend(flatten(i))
        elif i != None:
            f.append(i)
    return f
