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

print(silent_ratio('OSR_us_000_0010_8k.wav', 'Maciej'))
print(energy_entropy('zdanie.wav', 'Maciej', 5))

print(standard_deviation_of_zcr('zdanie.wav', 'Maciej'))
