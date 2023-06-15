from string import ascii_uppercase,digits
import random


class Robot:
    assigned_names = set()

    def reset(self):
        n = ""
        while not n or n in Robot.assigned_names:
            n = "".join(
                random.choices(ascii_uppercase, k=2) + random.choices(digits, k=3)
            )
        Robot.assigned_names.add(n)
        self.name = n

    def __init__(self):
        self.reset()
