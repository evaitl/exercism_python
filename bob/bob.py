def response(hey_bob):
    hey_bob = hey_bob.strip()
    silent = len(hey_bob) == 0
    question = hey_bob.endswith("?")
    yelling = hey_bob.isupper()
    match (silent, question, yelling):
        case (True, _, _):
            return "Fine. Be that way!"
        case (_, True, True):
            return "Calm down, I know what I'm doing!"
        case (_, True, False):
            return "Sure."
        case (_, False, True):
            return "Whoa, chill out!"
        case (_, False, False):
            return "Whatever."
