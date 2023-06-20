from itertools import count

_IDX=dict(zip("black brown red orange yellow green blue violet grey white".split(),count()))
_TOL={
    "grey": "0.05",
    "violet": "0.1",
    "blue": "0.25",
    "green": "0.5",
    "brown": "1",
    "red": "2",
    "gold": "5",
    "silver": "10",
}
_PREFIX = [
    (1e9, "giga"),
    (1e6, "mega"),
    (1e3, "kilo"),
    (1,""),
]

def resistor_label(colors):
    if len(colors) == 4:
        rv = (
        10 * _IDX[colors[0]] + _IDX[colors[1]]) * 10 ** _IDX[colors[2]]
    elif len(colors) == 5:
        rv = (100 * _IDX[colors[0]] + 10 * _IDX[colors[1]] + _IDX[colors[2]]) * 10 ** _IDX[colors[3]]
    else:
        return "0 ohms"
    tol = _TOL[colors[-1]]
    d,prefix = next((d,p) for (d,p) in _PREFIX if rv>=d)
    rv /= d
    
    return f"{rv:g} {prefix}ohms ±{tol}%"
