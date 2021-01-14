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
file_path = 'D:/project/web_layout_defect/defect_detect/data_generate/jiayi'
css_name = 'index.css'


# format the css files
files = os.listdir(file_path)
files = [file for file in files if file.endswith('_files')]
files = [os.path.join(file_path, os.path.join(f, css_name)) for f in files]   # list of css files for each webpage





# Re-format the css files for later parse
for file in files:   
    f = cssutils.parseFile(file, encoding='utf-8') # parse css file
    cssrules = f.cssRules   # list all Rules in css
    
    with open(file, 'w+', encoding='utf-8') as f:  # overwrite the global.css with formatted css stylesheet
        for rule in cssrules:
            text = rule.cssText   # Text of each css rule line by line
            for line in text:
                f.write(line)   # write to file line by line


# Read the css file and modify it to generate layout defect
for file in files:
    
    '''
    with open(file, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        
        for line in range(len(lines)):
            
            if '@media screen and (max-width: 768px) {' in lines[line]:
                if '.base-header .group-list.nav {' in lines[line + 1]:
                    
                    lines[line + 2] = '/* display: none */'
                    
    '''
    with open(file, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        
        for line in range(len(lines)):
            
            if '@media (max-width: 768px) {' in lines[line]:
                if '.menubg' in lines[line + 1]:
                    lines[line + 2] = '/* display: none */'

                
    with open(file, 'w', encoding='utf-8') as f:
        
        f.writelines(lines)
                    
                    
                    
     
                    
print('Finished editing.')



    









