from os import listdir
from os.path import isfile, join
from typing import Final

import numpy as np
from scipy.io import wavfile

### Windows size
SIZE: Final = 600
LEN_OF_FRAME: Final = 0.02

def flatten(t):
    return [item for sublist in t for item in sublist]

### Read all filenames
path_m = './samples/Maciej_Chylak/Znormalizowane'
path_d = './samples/Dawid_Janus/Znormalizowane'

all_filenames_m = [file for file in listdir(path_m) if isfile(join(path_m, file))]
all_filenames_d = [file for file in listdir(path_d) if isfile(join(path_d, file))]

data_dict = dict()
samplerate_dict = dict()


for file in all_filenames_m:
    key_dict = 'Maciej_' + file
    samplerate, data =  wavfile.read(path_m + '/' + file)
    size_of_frame = int(LEN_OF_FRAME * samplerate)

    data_splited = [data[x:x+size_of_frame] for x in range(0, len(data), size_of_frame)]

    data_dict[key_dict] = data_splited
    samplerate_dict[key_dict] = samplerate

# for file in all_filenames_d:sou
#     key_data_dict = 'Dawid_' + file
#     samplerate_dict[key_data_dict], data_dict[key_data_dict] =  wavfile.read(path_d + '/' + file)
