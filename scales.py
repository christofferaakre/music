import numpy as np

c = 2 ** (1 / 12)
base = 440

major_scale = [
    1, 
    c ** 2,
    c ** 4, 
    c ** 5, 
    c ** 7, 
    c ** 9, 
    c ** 11, 
    c ** 12
]

minor_scale = [
    1,
    c ** 2,
    c ** 3,
    c ** 5,
    c ** 7,
    c ** 8,
    c ** 10,
    c ** 12
]

harmonic_minor_scale = [
    1,
    c ** 2,
    c ** 3,
    c ** 5,
    c ** 7,
    c ** 9,
    c ** 11,
    c ** 12
]

scales = {
    "major": major_scale,
    "minor": minor_scale,
    "harmonic minor": harmonic_minor_scale
}