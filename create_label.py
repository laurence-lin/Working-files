import numpy as np
import pandas as pd

import os

import shutils



'''

Using pre-defined label for other similar image

Rules:
    width = 500, 600, 760 px. Each same width image have same label location
    Browsers: chrome, edge, firefox. Chrome & edge have same label location, firefox location = chrome location - 0.027


'''

path = 'D:/project/web_layout_defect/defect_detect/data_generate/hamastar/text_next_row/image'

files = os.listdir(path)
images = [file.split('.png')[0] for file in files if file.endswith('.png')] # name of all image(without .png)

image_no_label = [img for img in images if not os.path.isfile(os.path.join(path, img + '.txt'))] # image that haven't have label yet

for i in range(len(image_no_label)):
    
    img = image_no_label[i]
    
    scale = img.split('_')[1]
    browser = img.split('_')[-1]
    
    if scale == '500':
        origin_label = os.path.join(path, '0.html_500_chrome.txt')
    elif scale == '600':
        origin_label = os.path.join(path, '0.html_600_chrome.txt')
    elif scale == '760':
        origin_label = os.path.join(path, '0.html_760_chrome.txt')
    
    f = open(origin_label, 'r')
    label = f.readlines()
    f.close()
        
    if browser == 'firefox':
        
        classes, x, y, w, h = map(float, label[0].split(' '))
        y -= 0.027
        classes, x, y, w, h = map(str, [classes, x, y, w, h])
        label = ' '.join([classes, x, y, w, h])
      
    f = open(os.path.join(path, img + '.txt'), 'w+')
    f.writelines(label)
    f.close()
    









