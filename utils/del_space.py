import shutils
import os
import argparse

# Delete the last space line
'''
Remove the space postfix prefix for label.txt file

'''

argparser = argparse.ArgumentParser()  # Create parser
argparser.add_argument('-l', '--label_path',  # Add argument to this parser
                       action = 'store',   # store the arguments given to the parser
                       help='Path for label files that need to remove space postfix') # help message for this argument
args = argparser.parse_args() # parse arguments
args = vars(args)
label_path = args['label_path']

#label_path = 'D:/project/web_layout_defect/defect_detect/darknet/data/validate_jiayi'

files = [file  for file in os.listdir(label_path) if file.endswith('.txt') and not file.startswith('class')]
to_write = []

for file in files:
    with open(os.path.join(label_path,file), 'r+') as f:
        
        lines = f.readlines()
        
        lines[-1] = lines[-1].strip('\n') # remove the empty line in the last row: Don't jump to next row
        
        
    with open(os.path.join(label_path, file), 'w+') as f:
        f.writelines(lines)
        
print('Excluded all empty lines.')