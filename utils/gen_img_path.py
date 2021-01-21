import os
import cv2
import matplotlib.pyplot as plt
import skimage
import numpy as np
from PIL import Image


'''

Generate Image path list for train.txt for YOLO model
'''


img_path = 'D:/project/web_layout_defect/defect_detect/data_generate/hamastar/text_next_row/validate_img_hamastar' # image path
  
save_path = 'D:/project/web_layout_defect/defect_detect/darknet/data'   # path to save valid.txt


img_list = ['data/validate/{}\n'.format(file) for file in os.listdir(img_path) if file.endswith('.png')]
    
# save to valid.txt

with open(os.path.join(save_path, 'valid.txt'), 'w+') as f:
    f.writelines(img_list)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    