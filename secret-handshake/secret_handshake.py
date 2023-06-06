COMMANDS = ("wink", "double blink", "close your eyes", "jump")


def commands(binary_str):
    actions = [
        COMMANDS[i] for i, ch in enumerate(reversed(binary_str[1:])) if ch == "1"
    ]
    if binary_str[0] == "1":
        actions.reverse()
    return actions
