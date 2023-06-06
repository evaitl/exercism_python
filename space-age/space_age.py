class SpaceAge:
    PERIODS = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }
    SEC_PER_YEAR = 31557600

    def __init__(self, seconds):
        self.years = seconds / SpaceAge.SEC_PER_YEAR
        for planet, period in SpaceAge.PERIODS.items():
            setattr(self, "on_" + planet, lambda p=period: round(self.years / p, 2))
