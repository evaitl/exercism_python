def steps(number: int) -> int:
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0
    return 1 + steps(number / 2 if number % 2 == 0 else 3 * number + 1)
