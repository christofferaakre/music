import numpy as np

c = 2 ** (1 / 12)
base = 440

chromatic_scale = [
    1,
    c ** 1,
    c ** 2,
    c ** 3,
    c ** 4,
    c ** 5,
    c ** 6,
    c ** 7,
    c ** 8,
    c ** 9,
    c ** 10,
    c ** 11,

]

major_scale = [
    1, 
    c ** 2,
    c ** 4, 
    c ** 5, 
    c ** 7, 
    c ** 9, 
    c ** 11, 
]

minor_scale = [
    1,
    c ** 2,
    c ** 3,
    c ** 5,
    c ** 7,
    c ** 8,
    c ** 10,
]

harmonic_minor_scale = [
    1,
    c ** 2,
    c ** 3,
    c ** 5,
    c ** 7,
    c ** 8,
    c ** 11,
]

scales = {
    "major": major_scale,
    "minor": minor_scale,
    "harmonic minor": harmonic_minor_scale,
    "chromatic": chromatic_scale
}