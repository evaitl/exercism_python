def proverb(*lst, qualifier=None):
    if qualifier:
        qualifier = qualifier + " "
    else:
        qualifier = ""
    out = [
        f"For want of a {lst[i]} the {lst[i+1]} was lost." for i in range(len(lst) - 1)
    ]
    if lst:
        out.append(f"And all for the want of a {qualifier}{lst[0]}.")
    return out
