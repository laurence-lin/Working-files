import numpy as np
import pandas as pd

import os

from PIL import Image
import matplotlib.pyplot as plt
import cv2

import json
import sys, getopt
import argparse


'''

Validate the YOLO label could correctly draw the bounding box containing defect in image

'''


cmdargs = argparse.ArgumentParser()
cmdargs.add_argument('-i', '--img_path', action = 'store', help='Image Path')
parsed = cmdargs.parse_known_args()
kwargs, args = vars(parsed[0]), parsed[1] # non pair argument will go into args
# so now you can do
path = kwargs.get('img_path', '')

#path = 'D:/project/web_layout_defect/defect_detect/darknet/data/validate2'

# Test the auto-create label is valid
image_list = [file for file in os.listdir(path) if file.endswith('.png')]
image_list = [os.path.join(path, file) for file in image_list if file.split('_')[1] == '500']
label_list = [os.path.join(path, file.split('.png')[0] + '.txt') for file in image_list]


for i in range(len(image_list)):
    
    if i > 19:
        break

    img = image_list[i]
    label = label_list[i]

    label = open(label, 'r')
    lines = label.readlines()
    label.close()
    
    img = plt.imread(img)
    dh, dw, _ = img.shape
    
    for data in lines:
      _, x, y, w, h = map(float, data.split(' '))

      l = int((x - w/2)*dw)
      r = int((x + w/2)*dw)
      t = int((y - h/2)*dh)
      b = int((y + h/2)*dh)

      cv2.rectangle(img, (l, t), (r, b), (255, 0, 0), 1)

    
    plt.subplot(4, 5, i+1)
    plt.imshow(img)


plt.show()



'''
Validate model prediction label on the images

input: image path, 

'''

'''

arg_list = sys.argv[1:]

try:
    arguments, left_arg = getopt.getopt(arg_list, 'i:s:l:thr', ['img_path=', 'src_path=', 'label_path=', 'thresh='])
    
    for opt, value in arguments:
        if opt in ('-i', '--img_path'):
            img_path = value
            
        elif opt in ('-s', '--src_path'):
            src_img_path = value
            
        elif opt in ('-l', '--label_path'):
            label = value
            
        elif opt in ('-thr', '--thresh'):
            threshold = value
            
except getopt.error as err:
    print('error:', err)


print('img_path:', img_path)
print('src_img_path:', src_img_path)
print('label_path:', label)
print('Threshold:', threshold)

# Validate model prediction on validate images
#img_path = 'D:/project/web_layout_defect/defect_detect/data_generate/hamastar/text_next_row/validate_img_hamastar' # Image to validate performance
#src_img_path = 'D:/project/web_layout_defect/defect_detect/darknet'  # the file directory before "file name" in json
#label = 'D:/project/web_layout_defect/defect_detect/darknet/result_val.json'   # prediction result json file
#threshold = 0.5 # if object class confidence greater than threshold, than plot it

images = [os.path.join(img_path, file) for file in os.listdir(img_path) if file.endswith('.png')]

with open(label, 'r') as f:
    data = f.read()   #read content of result.json

results = json.loads(data)  # load json file content into python object: list


for i in range(len(results)):
    
    sample = results[i]
    img_name = os.path.join(src_img_path, sample['filename'])    
    img = plt.imread(img_name)
    dh, dw, _ = img.shape
          
    for obj in sample['objects']:
      
      if obj['confidence'] >= threshold:
          print('Confidence:', obj['confidence'])
          
          confidence = obj['confidence']
          x, y, w, h = obj['relative_coordinates'].values()
          label_name = obj['name']
          
        
          l = int((x - w/2)*dw)
          r = int((x + w/2)*dw)
          t = int((y - h/2)*dh)
          b = int((y + h/2)*dh)
        
          cv2.rectangle(img, (l, t), (r, b), (255, 0, 0), 1)
          cv2.putText(img, '{} {}'.format(label_name, str(confidence)), (l, t - 20), fontFace = cv2.FONT_HERSHEY_SIMPLEX, \
                    fontScale = 0.6, color = (255, 0, 0), thickness = 1)
        
        
        
    plt.figure(i)
    plt.imshow(img)
    plt.show()

'''
        
          
        































