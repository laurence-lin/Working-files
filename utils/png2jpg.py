from PIL import Image
import os
# 轉 jpg

png_path = 'D:/網頁比較/破版特徵偵測/defect1/images'

for img in os.listdir(png_path):
    if img.endswith(".png"):
        im = Image.open(f"{png_path}/{}".format(img))
        rgb_im = im.convert("RGB")
        img_name = img.split(".")[0]
        rgb_im.save(f"{png_path}/{}.jpg".format(img_name))
        
# 刪除原始 png 資料
for img in os.listdir(f"{png_path}/"):
    if img.endswith(".png"):
        os.remove(f"{png_path}/{}".format(img))