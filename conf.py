from os import listdir
from os.path import isfile, join
from typing import Final

from scipy.io import wavfile

### Read all filenames
path_m = './samples/Maciej_Chylak/Znormalizowane'
path_d = './samples/Dawid_Janus/Znormalizowane'

all_filenames_m = [file for file in listdir(path_m) if isfile(join(path_m, file))]
all_filenames_d = [file for file in listdir(path_d) if isfile(join(path_d, file))]
data_dict = dict()
samplerate_dict = dict()
for file in all_filenames_m:
    key_dict = 'Maciej_' + file
    samplerate_dict[key_dict], data_dict[key_dict] =  wavfile.read(path_m + '/' + file)
# for file in all_filenames_d:
#     key_data_dict = 'Dawid_' + file
#     samplerate_dict[key_data_dict], data_dict[key_data_dict] =  wavfile.read(path_d + '/' + file)

### Widnows size
size: Final = 600