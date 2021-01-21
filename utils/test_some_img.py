import os
import cv2
import matplotlib.pyplot as plt

import numpy


img_path = 'D:/project/web_layout_defect/defect_detect/data_generate/edu/txt_next_row/image_bin'
#img_path = 'C:/Users/lawrence123/downloads'

image_list = [os.path.join(img_path, file) for file in os.listdir(img_path) if file.endswith('.png')]

label_list = [file.replace('png', 'txt') for file in image_list]



for i in range(160, 260):
    
    
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


    fig_ind = int(i//4) + 1
    img_ind = int(i%4) + 1
    fig = plt.figure(fig_ind)
    ax = fig.add_subplot(2, 2, img_ind)
    ax.set_title(image_list[i].split('/')[-1])
    
    
    plt.imshow(img)
    plt.show()

