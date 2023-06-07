SCORES = {
    1: "aeioulnrst",
    2: "dg",
    3: "bcmp",
    4: "fhvwy",
    5: "k",
    8: "jx",
    10: "qz",
}
VALUES = {l: v for v in SCORES.keys() for l in SCORES[v]}


def score(word):
    return sum(VALUES[l] for l in word.strip().lower())
