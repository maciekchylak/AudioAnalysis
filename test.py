import os

from scipy.io import wavfile
from sound_functions import *

import numpy as np

samplerate, data =  read_wav('gyr.wav', 'Maciej')

print(volume(data))

print(volume_dynamic_range('Maciej'))
print(energy_entropy('Maciej', 10))
print(standard_deviation_of_zcr('Maciej'))

print(VSTD('Maciej'))