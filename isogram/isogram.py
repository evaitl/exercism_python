def is_isogram(string):
    chars = [ch for ch in string.lower() if ch.isalpha()]
    return len(set(chars)) == len(chars)
