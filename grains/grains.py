def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 1 if number == 1 else 2 * square(number - 1)


def total():
    return sum(square(x + 1) for x in range(64))
