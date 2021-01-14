from PIL import Image
import os



'''
After labeled several images, generate the label for left webpage automatically

'''

# Custom argument:
label_path = 'D:/project/web_layout_defect/defect_detect/data_generate/jiayi/txt_next_row'


labels = [file for file in os.listdir(label_path) if file.endswith('.txt') and len(file.split('_')) > 1]  # list of already exist labels
labels = [file.split('.txt')[0] for file in labels]

images = [file for file in os.listdir(label_path) if file.endswith('.png')]

for i in range(len(images)):
    
    img = images[i]
    img_name = img.split('.png')[0]
    browser = img_name.split('_')[-1]
    scale = img.split('_')[1]
    
    if not os.path.exists(os.path.join(label_path, img_name + '.txt')):
        
        for j in range(len(labels)):
            if scale == labels[j].split('_')[1]:
                if browser == labels[j].split('_')[-1]:
                    # create a copy label
                    with open(os.path.join(label_path, labels[j]+'.txt'), 'r+') as f:
                        data = f.readlines()
                        
                    with open(os.path.join(label_path, img_name + '.txt'), 'w+') as f:
                        f.writelines(data)
        
        
        
print('Finished creating label.')













