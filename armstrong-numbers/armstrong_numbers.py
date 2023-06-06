def is_armstrong_number(number):
    digits = len(str(number))
    return sum(int(ch) ** digits for ch in str(number)) == number
