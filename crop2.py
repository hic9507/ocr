import json
import os
import cv2, numpy as np
import matplotlib.pyplot as plt


base_label_path = 'D:/OCR/Training/label_Training_printed/'
base_image_path = 'D:/OCR/Training/ori_Training_printed/form/'

df_images = []

labeling_f = open('D:/new/ori/label.txt', 'w', encoding='utf-8')
count = 0



################################## json 파일 읽어오기
for q in os.listdir(base_label_path):
    num_folder = q
    # print(num_folder) # 001~050, print(q)도 똑같음
    for w in os.listdir(base_label_path + num_folder):
        label_file_name = w
         
        # print(label_file_name) ### 00110011001.json~05010103040.json

        ### 모든 폴더에 있는 json 파일 다 읽어와서 f에 저장. file > f로 변경
        f = (open(base_label_path + num_folder + '/' + label_file_name, 'r', encoding='utf-8'))
        file_json = json.load(f)

        for id in range(len(file_json['text']['word'])):
        
            bbox = file_json['text']['word'][id]['wordbox']


        # print(f) # <_io.TextIOWrapper name='D:/OCR/Training/label_Training_printed/001/00110042015.json' mode='r' encoding='utf-8'>
        # df_images.append((file_json['text']['word'][0]['wordbox'])) # [557, 251, 592, 312]
        # df_images.append((file_json['text']['word'])) # [[{'wordbox': [557, 251, 592, 312], 'value': '■', 'source': 'form', 'letter': [{'charbox': [559, 253, 590, 310], 'value': '■'}]} 이런 식으로 나옴
        # print('df_images: ', df_images) # df_images:  [[{'wordbox': [557, 251, 592, 312], 'value': '■', 'source': 'form', 'letter': [{'charbox': [559, 253, 590, 310], 'value': '■'}]}... 계속 나옴
        # print("file_json['text']['word']: ", file_json['text']['word']) #[{'wordbox': [557, 251, 592, 312], 'value': '■', 'source': 'form', 'letter': [{'charbox': [559, 253, 590, 310], 'value': '■'}]},...
        # print('------------------------')####


        # 이미지 이름 가져오기
            labeling = file_json['image']['file_name']
        # 이미지의 한 단어 가져오기
            value = file_json['text']['word'][id]['value']
        
            
            img = cv2.imread('D:/OCR/Training/ori_Training_printed/form/'+num_folder+'/'+labeling,0)


        # cv2.imshow('img', img)
        # cv2.waitKey()
        


            x = bbox[0]
            y = bbox[1]
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]


            crop_img = img[y:y+h, x:x+w]

            cv2.imwrite('D:/new/ori/002/' + labeling[:-4] + '_'+ str(count)+'.jpg', crop_img)

            labeling_f.write('D:/new/ori/002/' + labeling[:-4] + '_' +str(count)+'.jpg' +'\t' + value +'\n')

            count +=1
        # plt.imshow(crop_img, cmap=gray)
        # plt.show()

        
        # print('labeling: ', labeling) # 이미지 파일 이름 나옴
        # print('value: ', value) # 【서식...

# image =np.array([])

# ################################# 이미지 파일 읽어오기
# for q in os.listdir(base_image_path):
#     num_image = q
#     # print(num_image) # 001~050
#     for w in os.listdir(base_image_path + num_image):
#         image_file_name = w     
#         # print(image_file_name[:-4])  
#         # print(image_file_name) # 00110011001.jpg~05010103040.jpg
#         print('image file loding...')
#         load_image= cv2.imread(base_image_path + num_image + '/' +image_file_name) 


#         image = np.append(image, load_image)
#         print('i: ', i)
#     k = 0
    
#     for j in range(len(file_json['text']['word'])):
#         print(df_images[k][j]['wordbox'][0])
#         print(df_images[k][j]['wordbox'][1])
#         print(df_images[k][j]['wordbox'][2])
#         print(df_images[k][j]['wordbox'][3])

#         area = [df_images[k][j]['wordbox'][0], 
#                 df_images[k][j]['wordbox'][1], 
#                 df_images[k][j]['wordbox'][2], 
#                 df_images[k][j]['wordbox'][3]]
#                 #좌상단x, 좌상다ㄴy, 우하단x, 우하단y
       
#         # crop_img = load_image[area[1]:area[3], area[0]:area[2]]
#         # cv2.imshow('1', crop_img)
#         # cv2.waitKey()
#         # cv2.imwrite('D:/new/ori/002/' + image_file_name[:-4] + '_'+ '.jpg', crop_img)
#         # labeling_f.write('D:/new/ori/' + image_file_name[:-4] + '_' + labeling + '\t' + len(value) + '\n')
#         print('area: ', area)
#         print('k: ', k)
#         k += 1

# labeling_f.close()        