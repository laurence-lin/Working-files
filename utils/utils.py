import os


'''

Modify the downloaded file where error occurs while web scraping

'''

multi_files = 'D:/project/web_layout_defect/defect_detect/data_generate/mioali/txt_next_row'
files_path = [os.path.join(multi_files, file) for file in os.listdir(multi_files) if file.endswith('_files')]

for file_path in files_path:

  files = [file for file in os.listdir(file_path) if file.endswith('下載')]

  for file in files:
      origin = os.path.join(file_path, file)
      new_name = os.path.join(file_path, file[:-3])
    
      os.rename(origin, new_name)
    
    
  files = [file for file in os.listdir(file_path) if file.endswith('axd')]
  for file in files:
      origin = os.path.join(file_path, file)
      new_name = os.path.join(file_path, file.replace('axd', 'js'))
    
      os.rename(origin, new_name)
    