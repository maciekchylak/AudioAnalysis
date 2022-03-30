import os

from scipy.io import wavfile
from sound_functions import *

import numpy as np

samplerate, data =  read_wav('gyr.wav', 'Maciej')
samplerate, data = read_wav_clip('gyr.wav', 'Maciej')

v = volume('zdanie.wav', 'Maciej')
z = zero_crossing_rate('zdanie.wav', 'Maciej')
index_min_v = v.index(min(v))
print(v[index_min_v])
print(z[index_min_v])

print(low_short_time_energy_ratio('zdanie.wav', 'Maciej'))
