import re


class Luhn:
    reg = re.compile(r"(\d|\s)+")

    def __init__(self, card_num):
        mo = Luhn.reg.match(card_num)
        if mo and len(mo.group(0)) == len(card_num):
            card_num = [int(ch) for ch in card_num if ch.isdigit()]
            checksum = sum(
                (d if i % 2 == 0 else (2 * d if 2 * d <= 9 else 2 * d - 9))
                for i, d in enumerate(reversed(card_num))
            )
            self._valid = checksum % 10 == 0 and len(card_num) > 1
        else:
            self._valid = False

    def valid(self):
        return self._valid
