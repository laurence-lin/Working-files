import numpy as np
import pandas as pd
import os
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.firefox.options import Options as firefoxOp


'''
For the generated webpage with defect layout, create different scale: browser, browser size... etc for it, and take screenshot save as image

'''

# Custom argument: how to automatic set up argument?
data_path = 'D:/project/web_layout_defect/defect_detect/data_generate/jiayi' # directory of webpage files
save_path = 'D:/project/web_layout_defect/defect_detect/data_generate/jiayi/txt_next_row'  # directory of folder to save webpage screenshot

driver_path = 'D:/project/web_layout_defect/defect_detect/data_generate'   # directory of driver files

web_files = [(data_path + '/' + file) for file in os.listdir(data_path) if file.endswith('.html')]

# For next line defect, width should smaller than 768px
size = [800, 750, 600, 550]   # different width of screenshot
height = 700       # height of screenshot
   

# List three different browsers: Chrome, Firefox, Edge
driver_list = ['edge', 'firefox', 'chrome']

for driver_type in driver_list:
  
    # For all three web browsers
  if driver_type == 'edge':
      driver = webdriver.Edge(executable_path = os.path.join(driver_path, 'msedgedriver.exe'))
      
  elif driver_type == 'chrome':
      driver = webdriver.Chrome(executable_path = os.path.join(driver_path, 'chromedriver.exe'))
      
  elif driver_type == 'firefox':
      driver = webdriver.Firefox(executable_path=os.path.join(driver_path, 'geckodriver.exe'))
      
      
  for web in web_files: # For all 10 web pages
     
     save_name = web.split('/')[-1]  # origin webpage name to save as file name

     if driver_type == 'firefox':  # For firefox to read local file, need to add "file://" at the front
         web = 'file://' + web    

     driver.get(web)
     driver.set_window_size(size[0], height)
     time.sleep(3)
     driver.get_screenshot_as_file(os.path.join(save_path, f'{save_name}_{size[0]}_{driver_type}.png'))

     driver.set_window_size(size[1], height)
     time.sleep(3)
     driver.get_screenshot_as_file(os.path.join(save_path, f'{save_name}_{size[1]}_{driver_type}.png'))

     driver.set_window_size(size[2], height)
     time.sleep(3)
     driver.get_screenshot_as_file(os.path.join(save_path, f'{save_name}_{size[2]}_{driver_type}.png'))

  driver.quit()



















