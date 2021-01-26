from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOp

import os
import cv2
import matplotlib.pyplot as plt
import argparse
import time


'''

Allow the user to give testing parameters: url, web browser type, browser size
And perform web scraping to get screenshot image


'''



parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', action = 'store')
parser.add_argument('-s', '--size', action = 'store')
parser.add_argument('-b', '--browser', action = 'store')
parser.add_argument('-sv', '--save_path', action = 'store')
args = parser.parse_args()
args = vars(args)

#save_path = 'D:/web_testing' # path for saving the screenshot images for the scanned webpage

url = args['url']
width, height = str(args['size']).split(',')[0], str(args['size']).split(',')[1]
browser = args['browser'].lower()
save_path = args['save_path']

driver_path = '/mnt/d/project/web_layout_defect/defect_detect/data_generate'   # directory of driver files



if browser  == 'firefox':
    
    driver = webdriver.Firefox(executable_path=os.path.join(driver_path, 'geckodriver.exe'))
    
elif browser == 'chrome':
    Ops = chromeOp()
    Ops.add_argument('--headless')
    chromedriver_path = '/usr/bin/chromedriver' # chromedriver for WSL
    print('Driver path: ', chromedriver_path)
    driver = webdriver.Chrome(executable_path = chromedriver_path, options = Ops)
    
elif browser == 'edge':
    driver = webdriver.Edge(executable_path = os.path.join(driver_path, 'msedgedriver.exe'))
    
driver.get(url)
time.sleep(2)
driver.set_window_size(width, height)

element = driver.find_element_by_xpath('//*[@id="form1"]/div[2]/div/div/div/div[3]/div/div/div/div[3]')
links = [x.get_attribute('href') for x in element.find_elements_by_css_selector('a')]

for i in range(len(links)):
    link = links[i]
    #print('link:', link)
    #print(link.get_attribute('href'))
    driver.get(links[i])
    time.sleep(2)
    driver.get_screenshot_as_file('{}/{}_{}.png'.format(save_path, i, browser))
    time.sleep(2)
    
    if i > 20:
        break
    
print('Finished web scrapping. Prepare for web layout detection.')

driver.quit()
