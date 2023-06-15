class PhoneNumber:
    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"

    def __init__(self, number):
        if any(ch.isalpha() for ch in number):
            raise ValueError("letters not permitted")
        if any(ch in "@:!" for ch in number):  # A crap test, I know.
            raise ValueError("punctuations not permitted")
        n = "".join(ch for ch in number if ch.isdigit())
        if len(n) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(n) == 11:
            if n[0] == "1":
                n = n[1:]
            else:
                raise ValueError("11 digits must start with 1")
        if len(n) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if n[0] == "0":
            raise ValueError("area code cannot start with zero")
        if n[0] == "1":
            raise ValueError("area code cannot start with one")
        if n[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if n[3] == "1":
            raise ValueError("exchange code cannot start with one")
        self.number = n
        self.area_code = n[0:3]
