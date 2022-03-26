from os import listdir
from os.path import isfile, join

### Read all filenames
path_m = './samples/Maciej_Chylak/Znormalizowane'
path_d = './samples/Dawid_Janus/Znormalizowane'

all_filenames_m = [file for file in listdir(path_m) if isfile(join(path_m, file))]
all_filenames_d = [file for file in listdir(path_d) if isfile(join(path_d, file))]
