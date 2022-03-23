### There will be defined all sound features
import math
import numpy as np


def frequency(x):
    pass

def amplitude(x):
    pass

def volume(x):
    output = 0
    for el in x:
        output += amplitude(el) ** 2
    return math.sqrt(output / len(x))

def short_time_energy(x):
    return volume(x) ** 2

def zero_crossing_rate(x, sampl_freq):
    output = 0
    for i in range(1, len(x)):
        output += math.abs(
                            np.sign(amplitude(x[i])) - np.sign(amplitude(x[i - 1]))
                        )
    return (output * sampl_freq) / (len(x) * 2)
