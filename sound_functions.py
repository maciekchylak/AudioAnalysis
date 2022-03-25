### There will be defined all sound features
import math
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

def read_wav(filename):
    fs, data = wavfile.read(filename)
    return fs, data

def time_waveform(samplerate, data):
    length = len(data) / samplerate
    time = np.linspace(0., length, data.shape[0])

    plt.plot(time, data, label="Left channel")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()

def volume(data):
    output = 0
    for el in data:
        output += float(el) ** 2
    return math.sqrt(output / len(data))

def short_time_energy(data):
    return volume(data) ** 2

def zero_crossing_rate(data, samplerate):
    output = 0
    for i in range(1, len(data)):
        output += abs(
                            np.sign(float(data[i])) - np.sign(float(data[i - 1]))
                        )
    return (output * samplerate) / (len(data) * 2)
