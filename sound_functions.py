### There will be defined all sound functions
import math

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

from conf import *

### Frame level functions
def read_wav(filename, imie):
    if imie == 'Maciej':
        path = './samples/Maciej_Chylak/Znormalizowane'
    elif imie == 'Dawid':
        path = './samples/Dawid_Janus/Znormalizowane'
    else:
        return None

    path = path + '/' + filename

    return wavfile.read(path)

def read_all_wav_files(imie):
    output_list = [[], []]
    
    if imie == 'Maciej':
        all_filenames = all_filenames_m
    elif imie == 'Dawid':
        all_filenames = all_filenames_d
    else:
        return None
    
    for file in all_filenames:
        fs, data = read_wav(file, imie)
        output_list[0].append(fs)
        output_list[1].append(data)

    return output_list

def volume(filename, imie):
    _, data = read_wav(filename, imie)
    output = 0
    for el in data:
        output += float(el) ** 2
    return math.sqrt(output / len(data))

def energy(filename, imie):
    _, data = read_wav(filename, imie)
    output = 0
    for el in data:
        output += float(el) ** 2
    return output

def short_time_energy(filename, imie):
    _, data = read_wav(filename, imie)
    return volume(data) ** 2

def zero_crossing_rate(filename, imie):
    samplerate, data = read_wav(filename, imie)
    output = 0
    for i in range(1, len(data)):
        output += abs(
                            np.sign(float(data[i])) - np.sign(float(data[i - 1]))
                        )
    return (output * samplerate) / (len(data) * 2)

#TODO
def silent_ratio(data, filename):
    pass

def autocorelation(data, l):
    output = 0
    for i in range(len(data) - l):
        output += data[i] * data[i + l]
   
    return output

def average_magnitude_difference_function(data, l):
    output = 0
    for i in range(len(data) - l):
        output += abs(data[i + l] - data[i])
   
    return output

#TODO
def fundemental_frequency(data, filename):
    pass


### Clip level functions
def VSTD(imie):
    all_wav_files = read_all_wav_files(imie)
    list_of_volumes = [volume(frame) for frame in all_wav_files[1]]
    max_volume = max(list_of_volumes)
    list_of_volumes_norm = [el / max_volume for el in list_of_volumes]

    return np.std(list_of_volumes_norm)

def volume_dynamic_range(imie):
    list_of_volumes = []
    all_wav_files = read_all_wav_files(imie)
    for el in all_wav_files[1]:
        list_of_volumes.append(volume(el))
    return (max(list_of_volumes) - min(list_of_volumes)) / max(list_of_volumes)

#TODO
def volume_undulation():
    pass

### Energy level functions
def low_short_time_energy_ratio(imie):
    all_wav_files = read_all_wav_files(imie)
    N = len(all_wav_files[1])
    output = 0
    for el in all_wav_files[1]:
        output += abs(np.sign(0.5 * avSTE - short_time_energy(el)) + 1)
    
    return output / N

def energy_entropy(imie, K):
    all_wav_files = read_all_wav_files(imie)
    total_energy = energy(np.concatenate(all_wav_files[1]))
    
    output = 0
    for frame in all_wav_files[1]:
        frame_splited = np.array_split(ary = frame, indices_or_sections = K)
        for segment in frame_splited:
            normalized_energy = energy(segment) / total_energy
            output -= (normalized_energy ** 2) * math.log2(normalized_energy ** 2)
    
    return output


def standard_deviation_of_zcr(imie):
    all_wav_files = read_all_wav_files(imie)

    list_of_zcrs = [zero_crossing_rate(frame, samplerate) for samplerate, frame in zip(all_wav_files[0], all_wav_files[1])]

    return np.std(list_of_zcrs)

#TODO
def high_zero_crossing_rate_ratio(imie):
    all_wav_files = read_all_wav_files(imie)

    output = 0
    for frame in all_wav_files[1]:
        output += np.sign(zero_crossing_rate(frame) - 1.5 * avZCR) + 1
    
    return output / (2 * len(all_wav_files[1]))