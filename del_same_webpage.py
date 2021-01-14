import selenium 
from selenium import webdriver
import os
from PIL import Image
import matplotlib.pyplot as plt
import io
import time
import numpy as np
import io

'''
Read from webpage savepath,delete 1. Failed save webpage file 2. Webpage file that has same image appearance

'''

web_path = 'C:/Users/lawrence123/downloads'
webpages = [os.path.join(web_path, file) for file in os.listdir(web_path) if file.endswith('.html')]

driver_path = 'D:/project/web_layout_defect/defect_detect/data_generate/chromedriver.exe'
driver = webdriver.Chrome(executable_path = driver_path)

print('Start testing:')
driver.get(webpages[0])

image_list = []

for i in range(len(webpages)):
    
    page = webpages[i]
    
    try:
        driver.get(page)
        time.sleep(3)
        
        image = driver.get_screenshot_as_png() # get screenshots as byte object, instead of saving to disk
        image = Image.open(io.BytesIO(image))  # to read the byte object from byte
        image = np.array(image)
        
        for exist_img in image_list:
            if (image - exist_img).sum() < 1: # if two screenshot is same image, remove it
                print('Remove: ', page)
                os.remove(page)
                
        image_list.append(image)
                
        
    except Exception as ex:
        template = "Exception {0} occurred: {1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print('Occur at:', page)
        os.remove(page)
        
driver.quit()
