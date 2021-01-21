import numpy as np
import pandas as pd

import os

from selenium import webdriver
import cssutils

from bs4 import BeautifulSoup

'''
Modify the CSS of saved webpage to create standard defect layout.

'''


# parse the CSS file
# edit the CSS rules


# custom changes: How to set up arg?
file_path = 'D:/project/web_layout_defect/defect_detect/data_generate/miaoli/txt_next_row'

# format the css files
# list of css files for each webpage

css_list = []
for _file in os.listdir(file_path):
    if _file.endswith('_files'):
        
        web_files = '{}/{}'.format(file_path, _file)
        
        for css_file in os.listdir(web_files):
            if css_file.startswith('global'):
                
                css_list.append('{}/{}/{}'.format(file_path, _file, css_file))
                


# Re-format the css files for later parse
for file in css_list:   
    f = cssutils.parseFile(file, encoding='utf-8') # parse css file
    cssrules = f.cssRules   # list all Rules in css
    
    with open(file, 'w+', encoding='utf-8') as f:  # overwrite the global.css with formatted css stylesheet
        for rule in cssrules:
            text = rule.cssText   # Text of each css rule line by line
            for line in text:
                f.write(line)   # write to file line by line


# Read the css file and modify it to generate layout defect
for file in css_list:
    
    
    with open(file, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        
        for line in range(len(lines)):
            
            '''
            # Modify color
            if '.menubg .menuarea #menu li span a' in lines[line]:
                if 'color:' in lines[line + 6]:
                    #lines[line + 2] = '/* display: none; */'
                    lines[line + 6] = 'color: #343434;'
            
            '''
            
  
            if '@media screen and (max-width: 768px) {' in lines[line]:
                if '.base-header .group-list.nav {' in lines[line + 1]:
                    lines[line + 2] = '/* display: none */'
            '''      
            elif '@media (max-width: 560px) {' in lines[line]:
                if '.menubg' in lines[line + 1]:
                    lines[line + 2] = '/* display: none */'
                
            elif '@media (max-width: 1009px) and (min-width: 601px)' in lines[line]:
                if 'menubg' in lines[line + 1]:
                    lines[line + 2] = '/* display: none */'
                
            elif '@media (max-width: 600px) {' in lines[line]:
                if '.menubg' in lines[line + 1]:
                    lines[line + 2] = '/* display: none */'
                    
            elif '.content {' in lines[line]:
                if 'overflow: hidden' in lines[line + 1]:
                #if 'background-color: #fff' in lines[line + 2]:
                    lines[line + 1] = 'overflow: hidden; background-color: rgb(10, 150, 10);'

              '''  
    with open(file, 'w', encoding='utf-8') as f:
        
        f.writelines(lines)
                    
                    
                    
     
                    
print('Finished editing.')



    









