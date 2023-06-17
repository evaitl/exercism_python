from itertools import zip_longest


def transpose(lines):
    return "\n".join(
        "".join(o).rstrip("$").replace("$", " ")
        for o in zip_longest(*lines.splitlines(), fillvalue="$")
    )
