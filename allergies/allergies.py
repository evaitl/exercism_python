from itertools import count


class Allergies:
    AL = dict(
        (s, 2**i)
        for (s, i) in zip(
            "eggs peanuts shellfish strawberries tomatoes chocolate pollen cats".split(),
            count(),
        )
    )

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return (Allergies.AL[item] & self.score) != 0

    @property
    def lst(self):
        return [k for k in Allergies.AL if self.allergic_to(k)]
