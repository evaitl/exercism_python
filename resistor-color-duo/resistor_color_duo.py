from enum import Enum

Colors = Enum(
    "Colors", "black brown red orange yellow green blue violet grey white", start=0
)


def value(colors):
    return Colors[colors[0]].value * 10 + Colors[colors[1]].value
