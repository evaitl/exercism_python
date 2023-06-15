def is_paired(input_string):
    def matching(ch1, ch2):
        match (ch1, ch2):
            case ("(", ")"):
                return True
            case ("[", "]"):
                return True
            case ("{", "}"):
                return True
        return False

    stack = []
    for ch in (i for i in input_string if i in "[]{}()"):
        match ch:
            case "(" | "{" | "[":
                stack.append(ch)
            case m:
                if stack and matching(stack[len(stack) - 1], m):
                    stack.pop()
                else:
                    return False
    return not stack
