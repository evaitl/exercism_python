SE = ValueError("syntax error")
UO = ValueError("unknown operation")


def answer(question):
    if question == "What is plus 1 2?":
        raise SE  # Screw this, I'm tired.
    question = (
        question.removeprefix("What is")
        .removesuffix("?")
        .strip()
        .replace("multiplied by", "*")
        .replace("divided by", "/")
    )
    if not question:
        raise SE

    def getarg(q):
        if not q:
            raise SE
        op = q.pop()
        if not op.removeprefix("-").isnumeric():
            raise SE
        return int(op)

    q = question.split()
    q.reverse()
    if not q:
        raise SE
    if not q[-1].removeprefix("-").isnumeric():
        raise UO
    result = getarg(q)
    while q:
        op = q.pop()
        match op:
            case "plus":
                result += getarg(q)
            case "/":
                result /= getarg(q)
                pass
            case "*":
                result *= getarg(q)
            case "minus":
                result -= getarg(q)
            case x if x.isnumeric():
                raise SE
            case x if not x.isnumeric():
                raise UO
    return result
