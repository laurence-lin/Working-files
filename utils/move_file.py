import shutils
import os

path = 'file_path'

save_path = 'save_path'

files = [os.path.join(path, file) for file in path if 'ham' in file]

for file in files:

     shutils.move(os.path.join(path, file), os.path.join(save_path, file))