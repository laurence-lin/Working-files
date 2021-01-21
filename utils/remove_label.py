import shutils
import os
import argparse

'''

Remove all label files in a directory


'''

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--label_path', action='store', help='Path for location of labels to delete')
args = parser.parse_args() # Parse the argument: return namespace object
args = vars(args) # Convert namespace object to dictionary
label_path = args['label_path']

label_files = [os.path.join(label_path, file) for file in os.listdir(label_path) if file.endswith('.txt') and 'class' not in file]


for file in label_files:

     os.remove(file)