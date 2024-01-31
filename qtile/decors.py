# Qtile extras decorations for widgets (https://qtile-extras.readthedocs.io/en/stable/manual/how_to/decorations.html)
from qtile_extras.widget import decorations
from colors import *

# WIDGET DECORATIONS
# Decoration for widget texts
dectext = {
    "decorations": [
        decorations.RectDecoration(
            colour=colors_bg[3],
            radius=5,
            filled=True,
            padding_y=3,
            padding_x=0.5,
            extrawidth=0,
        )
    ],
}
# Decoration for layout widget
declayout = {
    "decorations": [
        decorations.RectDecoration(
            colour=colors_fg[7],
            radius=5,
            filled=True,
            padding_y=3,
            padding_x=0.5,
            extrawidth=0,
        )
    ],
}
# Decoration for battery widget
decbattery = {
    "decorations": [
        decorations.RectDecoration(
            colour=colors_fg[8],
            radius=5,
            filled=True,
            padding_y=3,
            padding_x=0.5,
            extrawidth=0,
        )
    ],
}
# Decoration for wifi widget
decwifi = {
    "decorations": [
        decorations.RectDecoration(
            colour=colors_fg[5],
            radius=5,
            filled=True,
            padding_y=3,
            padding_x=0.5,
            extrawidth=4,
        )
    ],
}
# Decoration for time and date widget
decdate = {
    "decorations": [
        decorations.RectDecoration(
            colour=colors_fg[0],
            radius=5,
            filled=True,
            padding_y=3,
            padding_x=0.5,
            extrawidth=4,
        )
    ],
}
# Decoration for volume widget
decvol = {
    "decorations": [
        decorations.RectDecoration(
            colour=colors_fg[3],
            radius=5,
            filled=True,
            padding_y=3,
            padding_x=0.5,
            extrawidth=4,
        )
    ],
}
# Decoration for brightness widget
declight = {
    "decorations": [
        decorations.RectDecoration(
            colour=colors_fg[4],
            radius=5,
            filled=True,
            padding_y=3,
            padding_x=0.5,
            extrawidth=5,
        )
    ],
}
# Decoration for keylock widget
deckeyboard = {
    "decorations": [
        decorations.RectDecoration(
            colour=colors_fg[9],
            radius=5,
            filled=True,
            padding_y=3,
            padding_x=0.5,
            extrawidth=5,
        )
    ],
}

# BAR LAYOUT DECORATIONS
# Semicircle that goes from left to right
powerline_left = {
    "decorations": [
        decorations.PowerLineDecoration(
            path='rounded_left'
        )
    ]
}
# Semicircle that goes from right to left
powerline_right = {
    "decorations": [
        decorations.PowerLineDecoration(
            path='rounded_right'
        )
    ]
}