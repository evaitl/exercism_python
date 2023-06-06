def convert(number):
    result = "".join(
        noise
        for divisor, noise in [(3, "Pling"), (5, "Plang"), (7, "Plong")]
        if number % divisor == 0
    )
    return result or str(number)
