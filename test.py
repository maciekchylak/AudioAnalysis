import os

from scipy.io import wavfile
from sound_functions import *

import numpy as np

samplerate, data =  read_wav('./Znormalizowane/gyr.wav')
print(len(data))
length = len(data) / samplerate
print(length)
print(np.linspace(0., length, data.shape[0]))

print(volume(data))

print(zero_crossing_rate(data, samplerate))