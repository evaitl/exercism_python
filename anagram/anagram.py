def find_anagrams(word, candidates):
    word = word.lower()
    sword = sorted(word)
    return [w for w in candidates if word != w.lower() and sword == sorted(w.lower())]
