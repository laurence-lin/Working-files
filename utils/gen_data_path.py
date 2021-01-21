import numpy as np
import pandas as pd

import os

import json


import sys, getopt
import argparse

'''

Generate train.txt for darknet model
function: 
    read text file txt, 
    open the image file path, 
    pass all image path to text file, 
    save updated text file

input: text file path, image file path

img_path: dir_to_img_folder
txt_path: txt_folder/train.txt

'''

cmdargs = argparse.ArgumentParser()
cmdargs.add_argument('-i', '--img_path', action = 'store', help='Image Path')
cmdargs.add_argument('-t', '--txt_path', action='store', help='Txt Path')
parsed = cmdargs.parse_known_args()
kwargs, args = vars(parsed[0]), parsed[1] # non pair argument will go into args
# so now you can do
img_path = kwargs.get('img_path', '')
txt_path = kwargs.get('txt_path', '')

filename = img_path.split('/')[-1]
sub_path = 'data/'+ filename


images = os.listdir(img_path)
images = [(sub_path + '/' + file + '\n') for file in images if file.endswith('.png')]

with open(txt_path, 'w+') as f:
    f.writelines(images)


























