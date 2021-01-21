import os
import cv2
import matplotlib.pyplot as plt
import skimage
import numpy as np
from PIL import Image
import os
import sys, getopt
import argparse
from matplotlib import cm

# Image processing: 
    # transform image to model acceptable size, transform to gray, binarization
    
    
current_dir = os.getcwd()

# get input argument:
    
cmdargs = argparse.ArgumentParser()
cmdargs.add_argument('-i', '--img_path', action = 'store', help='Image Path')
cmdargs.add_argument('-s', '--save_path', action='store', help='Save Path')
parsed = cmdargs.parse_known_args()
kwargs, args = vars(parsed[0]), parsed[1] # non pair argument will go into args
# so now you can do
img_path = kwargs.get('img_path', '')
save_path = kwargs.get('save_path', '')


img_list = os.listdir(img_path)
img_list = [file for file in img_list if file.endswith('.png')]


def transform_size(img):
    # img: PIL Image object
    # return: image size with width and height product of 32
    w, h = img.size
    
    w_new = w - w%32 # make w, h dividable by 32, for YOLO model architecture
    h_new = h - h%32
    
    img = img.resize((w_new, h_new))
    
    return img


def color2gray(img):
    # img: PIL image object
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img


def binarize(img):
    # img: PIL image object
    img = np.array(img)
    edge = cv2.Canny(img, 0, 127)
    
    
    return edge

def blur(img):
    
    return cv2.GaussianBlur(img, (3, 3), 0)
    



for i in img_list:
    img = Image.open(os.path.join(img_path, i))
    img = transform_size(img)
    img = binarize(img)
    img = blur(img)
    
    img = Image.fromarray(np.uint8(cm.gist_earth(img)*255))

    img.save(f"{save_path}/{i}")



'''
# Convert png image to jpg image
for img in os.listdir(png_path):
    if img.endswith(".png"):
        im = Image.open(f"{png_path}/{}".format(img))
        rgb_im = im.convert("RGB")
        img_name = img.split(".")[0]
        rgb_im.save(f"{png_path}/{}.jpg".format(img_name))
        
# 刪除原始 png 資料
for img in os.listdir(f"{png_path}/"):
    if img.endswith(".png"):
        os.remove(f"{png_path}/{}".format(img))
'''
        



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    