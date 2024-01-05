import json
import io, os
import cv2, glob, numpy as np

base_path = 'D:/OCR/Training/label_Training_printed/001/'
file =[]
df_images = []

gt_train_file = open('D:/deep-text-recognition-benchmark/data/gt_train.txt', 'w')
gt_validation_file = open('D:/deep-text-recognition-benchmark/data/gt_validation.txt', 'w')
gt_test_file = open('D:/deep-text-recognition-benchmark/data/gt_test.txt', 'w')

for filename in os.listdir(base_path):
    file = json.load(open(base_path + filename, encoding='utf-8'))  
    df_images.append((file['text']['word']))

image =np.array([])
# k = 0

for i in (os.listdir('D:/OCR/Training/ori_Training_printed/form/001/')):
    path = 'D:/OCR/Training/ori_Training_printed/form/001/' + i
    img = cv2.imread(path)
    # cv2.imshow('1', img)
    # cv2.waitKey()

    image = np.append(image, img)
    # print('i: ', i)
    k = 0
    
    for j in range(len(file['text']['word'])):
        
        area = [df_images[k][j]['wordbox'][0], 
                df_images[k][j]['wordbox'][1], 
                df_images[k][j]['wordbox'][2], 
                df_images[k][j]['wordbox'][3]]
        
                #좌상단x, 좌상다ㄴy, 우하단x, 우하단y
       
        crop_img = img[area[1]:area[3], area[0]:area[2]]
        cv2.imshow('1', crop_img)
        cv2.waitKey()
        cv2.imwrite('D:/new/ori/001/' + str(k) + i, crop_img)
        # gt
        k += 1
        # print('k: ', k)