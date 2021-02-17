cd utils

python web_testing.py --url https://www.hamastar.com.tw --size 1200,800 --browser chrome  --save_path /mnt/d/project/web_layout_defect/defect_detect/darknet/data/web_testing

python process_image.py --img_path /mnt/d/project/web_layout_defect/defect_detect/darknet/data/web_testing --save_path /mnt/d/project/web_layout_defect/defect_detect/darknet/data/web_test_bin

python gen_test_label.py --img_path /mnt/d/project/web_layout_defect/defect_detect/darknet/data/web_test_bin

python gen_data_path.py --img_path /mnt/d/project/web_layout_defect/defect_detect/darknet/data/web_test_bin --txt_path /mnt/d/project/web_layout_defect/defect_detect/darknet/data/test.txt

cd /mnt/d/project/web_layout_defect/defect_detect/darknet

./darknet detector test data/obj.data cfg/yolov4-tiny_1c.cfg backup/yolov4-tiny_1c_best.weights -ext_output -dont_show -thresh 0.5 -out result.json < data/test.txt
