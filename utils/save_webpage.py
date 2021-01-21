import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOp
import os
import pandas as pd
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import pyautogui


'''
尚無法指定儲存位置
'''

save_path = 'D:/project/web_layout_defect/defect_detect/data_generate/hamastar/text_next_row/validate_web_hamastar'

k = 0
def save_webpage(name, k):
    # type on keyboard to download whole webpage
    # name: the webpage.html name to save
    pyautogui.keyDown('ctrl')
    pyautogui.press('s')
    pyautogui.keyUp('ctrl')
    time.sleep(2)

    #pyautogui.hotkey('ctrl' + 'space') # change to english input
  
    time.sleep(1)
       
    k += 1

    pyautogui.typewrite(name)
    pyautogui.press('enter')
    
    return k

'''
# These webpages for training

def start(driver):
    #最新消息
    driver.find_element_by_xpath('//*[@id="Group_7_twhKIKGLIq"]/div/div[1]/div/h3/span/a').click()
    time.sleep(1)
    save_webpage('0.html')

# define the webpages we want to get
def first(driver):
    # 哈瑪星防疫
    driver.find_element_by_xpath('//*[@id="CCMS_Content"]/div/div/div/div[3]/div/div/div/ul/li[2]/div/div/div/div/a/div[1]/span').click()
    time.sleep(1)
    
    save_webpage('1.html')
    
    
def second(driver):
    # 關於哈瑪星
    driver.find_element_by_xpath('//*[@id="Group_17_bpRqiewYWo"]/div/div[1]/div/h3/span/a').click()
    time.sleep(1)
    
    save_webpage('2.html')

def third(driver):
    # 資訊安全管理政策
    driver.find_element_by_xpath('//*[@id="CCMS_Content"]/div/div/div/div[1]/div/div/div/ul/li[6]/span/a').click()
    time.sleep(1)
    
    save_webpage('3.html')
    
def fourth(driver):
    #產品服務
    driver.find_element_by_xpath('//*[@id="Group_33_WRMrbdnbTt"]/div/div[1]/div/h3/span/a').click()
    time.sleep(1)
    
    save_webpage('4.html')
    
def fifth(driver):
    # Magic VR
    driver.find_element_by_xpath('//*[@id="CCMS_Content"]/div/div/div/div[2]/div/div/div/ul/li[2]/div/div/div/div/a/div[1]/span').click()
    time.sleep(1)
    
    save_webpage('5.html')

def sixth(driver):
    #專案服務
    driver.find_element_by_xpath('//*[@id="Group_24_XdNqXXXKGC"]/div/div[1]/div/h3/span/a').click()
    time.sleep(1)
    
    save_webpage('6.html')
    
def seventh(driver):
    #專案服務
    driver.find_element_by_xpath('//*[@id="Group_31_xWXBPYYTqa"]/div/div[1]/div/h3/span/a').click()
    time.sleep(1)
    
    save_webpage('7.html')
    
def eighth(driver):
    #企劃雲端服務
    driver.find_element_by_xpath('//*[@id="Group_26_MIbvGhtTID"]/div/div[1]/div/h3/span/a').click()
    time.sleep(1)
    
    save_webpage('8.html')
    
def ninth(driver):
    #企業社會責任
    driver.find_element_by_xpath('//*[@id="Group_28_WfoaCqqBeH"]/div/div[1]/div/h3/span/a').click()
    time.sleep(1)
    
    save_webpage('9.html')


#Chrome
driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
html = driver.get(all_urls[0])

start(driver)
time.sleep(2)
first(driver)
time.sleep(2)
second(driver)
time.sleep(2)
third(driver)
time.sleep(2)
fourth(driver)
time.sleep(2)
fifth(driver)
time.sleep(2)
sixth(driver)
time.sleep(2)
seventh(driver)
time.sleep(2)
eighth(driver)
time.sleep(2)
ninth(driver)

#driver.quit()
'''
'''

# These webpage is for validation

def start(driver):
    #最新消息-清寒學生
    driver.find_element_by_xpath('//*[@id="Group_7_vkgWqevmLV"]/div/div[1]/div/h3/span/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="CCMS_Content"]/div/div/div/div[3]/div/div/div/ul/li[3]/div/div/div/div/a/div[1]/span').click()
    time.sleep(3)
    save_webpage('0.html')

# define the webpages we want to get
def first(driver):
    # 清寒學生-滑到底
    driver.execute_script("window.scrollTo(0, 800)")
    time.sleep(3)
    
    save_webpage('1.html')
    
    
def second(driver):
    # 關於哈瑪星
    driver.execute_script('window.scrollTo(0, 1600)')
    time.sleep(3)
    save_webpage('2.html')

def third(driver):
    # 最新消息-媒體報導
    driver.find_element_by_xpath('//*[@id="Group_7_vkgWqevmLV"]/div/div[1]/div/h3/span/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="CCMS_Content"]/div/div/div/div[2]/div/div/div/ul/li[3]/span/a').click()
    time.sleep(3)
    save_webpage('3.html')
    
def fourth(driver):
    # 媒體報導: 資安及國安
    driver.find_element_by_xpath('//*[@id="CCMS_Content"]/div/div/div/div[3]/div/div/div/ul/li[6]/div/div/div/div/a/div[1]/span').click()
    time.sleep(3)
    
    save_webpage('4.html')
    
def fifth(driver):
    # 產品服務: ClassHub
    driver.find_element_by_xpath('//*[@id="Group_33_dNofTktKoG"]/div/div[1]/div/h3/span/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="CCMS_Content"]/div/div/div/div[2]/div/div/div/ul/li[3]/div/div/div/div/a/div[1]/span').click()
    time.sleep(3)
    
    save_webpage('5.html')

def sixth(driver):
    #專案服務: ISRM 資安風險平台
    driver.find_element_by_xpath('//*[@id="Group_24_vGexYUYBge"]/div/div[1]/div/h3/span/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="CCMS_Content"]/div/div/div/div[2]/div/div/div/div/ul/li[3]/div/ul/li[1]/a[1]/img').click()
    time.sleep(3)
    save_webpage('6.html')
    
def seventh(driver):
    #專案服務: ISRM: 聯絡我們
    driver.find_element_by_xpath('//*[@id="CCMS_Content"]/div/div/div/div[1]/div/div/div/ul/li[3]/span/a').click()
    time.sleep(3)
    
    save_webpage('7.html')
    
def eighth(driver):
    #我們的客戶: 地方縣市政府
    driver.find_element_by_xpath('//*[@id="Group_26_GYFaAdEetd"]/div/div[1]/div/h3/span/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="CCMS_Content"]/div/div/div/div[2]/div/div/div/ul/li[3]/span/a').click()
    time.sleep(3)
    save_webpage('8.html')
    
def ninth(driver):
    #企業社會責任: 綠色環保目標
    driver.find_element_by_xpath('//*[@id="Group_28_jfhisNyPLn"]/div/div[1]/div/h3/span/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="base-content"]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/ul/li[3]/span/a').click()
    time.sleep(3)
    save_webpage('9.html')


#Chrome
driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
html = driver.get(all_urls[0])

start(driver)
time.sleep(2)
first(driver)
time.sleep(2)
second(driver)
time.sleep(2)
third(driver)
time.sleep(2)
fourth(driver)
time.sleep(2)
fifth(driver)
time.sleep(2)
sixth(driver)
time.sleep(2)
seventh(driver)
time.sleep(2)
eighth(driver)
time.sleep(2)
ninth(driver)

#driver.quit()
'''

'''
# JiaYi
url = 'D:/project/web_layout_defect/defect_detect/data_generate/jiayi/嘉義縣政府全球資訊網.html' # parent webpage to navigate to more pages

driver_path = 'D:/project/web_layout_defect/defect_detect/data_generate/chromedriver.exe'
driver = webdriver.Chrome(executable_path = driver_path)
html = driver.get(url)

pages_1 = driver.find_elements_by_xpath('//*[@id="footermenu"]/div[6]/ul//a[@href]')
pages_2 = driver.find_elements_by_xpath('//*[@id="footermenu"]/div[3]/ul//a[@href]')

pages_1 = [elem.get_attribute('href') for elem in pages_1]
pages_2 = [elem.get_attribute('href') for elem in pages_2]

n_pages = 10
page_count = 0
for i in range(5):
    
    driver.get(pages_1[i])
    time.sleep(3)
    page_count += 1
    
    print('Save page:', str(page_count) + '.html')
    save_webpage('{}.html'.format(page_count))
    
for j in range(5):
    driver.get(pages_2[j])
    time.sleep(3)
    page_count += 1
    
    print('Save page:', str(page_count) + '.html')
    save_webpage('{}.html'.format(page_count))
'''
    
'''
# Nantou
# Could not get webpage for same layout style automatically, need to search by xpath
url = 'D:/project/web_layout_defect/defect_detect/data_generate/nantou/南投縣政府 Nantou County Government.html' # parent webpage to navigate to more pages

driver_path = 'D:/project/web_layout_defect/defect_detect/data_generate/chromedriver.exe'
driver = webdriver.Chrome(executable_path = driver_path)
html = driver.get(url)

page1 = driver.find_elements_by_xpath('/html/body/div/footer/div/div/div/div[7]/ul//a[@href]')
page2 = driver.find_elements_by_xpath('/html/body/div/footer/div/div/div/div[2]/ul//a[@href]')
page3 = driver.find_elements_by_xpath('/html/body/div/footer/div/div/div/div[5]/ul//a[@href]')
page4 = driver.find_elements_by_xpath('/html/body/footer/div/div/div/div[8]/ul//a[@href]')

links = [elem.get_attribute('href') for elem in page1]
links.extend([elem.get_attribute('href') for elem in page2])
links.extend([elem.get_attribute('href') for elem in page3])
links.extend([elem.get_attribute('href') for elem in page4])

print('Total links: ', len(links))

print('Start web scraping!')

n_pages = 35
page_count = 0
for i in range(n_pages):
    
    driver.get(links[i])
    time.sleep(8)
    page_count += 1
    
    print('Save page:', str(page_count) + '.html')
    save_webpage('{}.html'.format(page_count))
    

driver.quit()
    
'''
'''
# Taichung
url = 'D:/project/web_layout_defect/defect_detect/data_generate/taichung/臺中市政府全球資訊網.html' # parent webpage to navigate to more pages

driver_path = 'D:/project/web_layout_defect/defect_detect/data_generate/chromedriver.exe'
driver = webdriver.Chrome(executable_path = driver_path)
html = driver.get(url)

driver.find_element_by_xpath('//*[@id="goCenter"]').click()
time.sleep(3)
driver.maximize_window()
time.sleep(3)

page1 = driver.find_elements_by_xpath('//*[@id="header"]/nav[2]/ul//a[@href]')
page2 = driver.find_elements_by_xpath('/html/body/div[1]/footer/nav/ul/li[2]/ul//a[@href]')
page3 = driver.find_elements_by_xpath('/html/body/div[1]/footer/nav/ul/li[3]/ul//a[@href]')
page4 = driver.find_elements_by_xpath('/html/body/div[1]/footer/nav/ul/li[4]/ul//a[@href]')
page5 = driver.find_elements_by_xpath('/html/body/div[1]/footer/nav/ul/li[5]/ul//a[@href]')

links = [elem.get_attribute('href') for elem in page1]
links.extend([elem.get_attribute('href') for elem in page2])
links.extend([elem.get_attribute('href') for elem in page3])
links.extend([elem.get_attribute('href') for elem in page4])
links.extend([elem.get_attribute('href') for elem in page5])



links = [web for web in links if web.startswith('https://www.taichung.gov.tw/')] # Don't get the popup links

print('Total links: ', len(links))

print('Start web scraping!')

n_pages = 50
page_count = 0
for i in range(n_pages):
    
    try:
      driver.get(links[i])
      time.sleep(10)
      page_count += 1
    
      print('Save page:', str(page_count) + '.html')
      save_webpage('{}.html'.format(page_count))
    
    except Exception as err:
      print('Exception error: ', err)
      print('Exception at {} pages'.format(page_count))
      break

driver.quit()
'''


# Wait for timeout seconds until the webpages is saved
def download_wait(download_directory, timeout, nfiles = None):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(download_directory)
        files = [file for file in files if file.endswith('.html')]
        if nfiles and len(files) != nfiles:
            dl_wait = True
            
        for fname in files:
            if fname.endswith('.html'):
                dl_wait = True
                
        seconds += 1
        
    return seconds
        
        
        


#Pindong
url = 'https://www.miaoli.gov.tw/' # parent webpage to navigate to more pages
save_path = 'C:/Users/lawrence123/downloads'
driver_path = 'D:/project/web_layout_defect/defect_detect/data_generate/chromedriver.exe'
driver = webdriver.Chrome(executable_path = driver_path)
html = driver.get(url)

driver.maximize_window()
time.sleep(3)

links = driver.find_elements_by_xpath('//a[@href]')
links = [elem.get_attribute('href') for elem in links]
links = [web for web in links if web.startswith('https://www.miaoli.gov.tw/')] # Don't get the popup links, get the web links that have same website name
links = list(set(links))

print('Total links: ', len(links))

print('Start web scraping!')


n_pages = 30
page_count = 0
for i in range(n_pages):
    
    try:
      print('Get link: ', links[i])
      driver.get(links[i])
      time.sleep(3)
      page_count += 1
    
      print('Save page:', str(i) + '.html')
      k = save_webpage('{}.html'.format(i), k)
      download_wait(save_path, 8, n_pages)
    
    except Exception as err:
      print('Exception error: ', err)
      print('Exception at {} pages'.format(page_count))
      break

#driver.quit()







