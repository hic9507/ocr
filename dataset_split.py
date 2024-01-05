# import os
# import json
# import splitfolders
# import cv2

# with open('D:/label.txt', 'r', encoding='utf-8') as f:
#     files = f.readlines()
   
# # path = 'D:/data'
# # train_txt = os.path.join(path, 'train_gt.txt')
# # valid_txt = os.path.join(path, 'valid_gt.txt')
# # f=open(train_txt)
# # lines = f.readlines()
# # f.close()

# f_train = open(train_gt.txt, mode='wt', encoding='utf-8')
# f_valid  = open(valid_gt.txt, mode='wt', encoding='utf-8')

# for i in range(len(lines)):
#     if i % 20 == 0:
#         f_valid.write(lines[i])
#     else:
#         f_train.write(lines[i])

# # print(files)
# n_samples = len(files) # 9546600
# n_train = int(n_samples * 0.8)
# n_valid = int(n_samples * 0.2)
# # print(n_train) # 7637280
# # print(n_valid) # 1909320

# # move_files = []
# # for i in len(int(n_valid)):
# #     if file.endswith('.jpg'):
# #         move_files.append(file)
# #     shutil.move('D:/OCR_clop/'+ move_files,  'D:/data/validation/'+ move_files)





# # # files.split()

# # for id in files:

# # splitfolders.ratio('D:/OCR_clop/', 'D:/deep-text-recognition-benchmark/data/', seed=77, ratio=(0.8, 0.2), group_prefix=2)


##################################################################### label.txt 8:2 비율로 나누기 시작 ##################################################################################


import os
import cv2
import random
import shutil

labeling_valid_f = open('D:/data/valid_gt.txt', 'a', encoding='utf-8') # 'a'도 되고 'w'도 되는데 새로 만들 땐 w로
labeling_train_f = open('D:/data/train_gt.txt', 'a', encoding='utf-8')

with open('D:/label_leak1118.txt', 'r', encoding='utf-8') as f:
    files = f.readlines()
    
# n_samples = len(files) - 2977599 -5 # 9546600
n_samples = len(files)
n_train = int(n_samples * 0.4) # 7637276
n_valid = int(n_samples * 0.6) # 1909319
print(n_samples, n_train, n_valid)


for _ in range(n_train):

    x = len(files)

    try:
        r_label = files.pop(random.randint(0,x-1))
        # print(r_label)
        line_list = r_label.split('/t')
        labeling_train_f.write(r_label)
        img_path = line_list[0]
        image_path = img_path.split('\t')
    #     print(image_path)
    #     print('='*100)
    # shutil.move(image_path[0], 'D:/data/train/'+ img_path[12:])
        shutil.move(image_path[0], 'D:/data/train/'+ image_path[0][12:])


        # shutil.move(img_path, train_dir+ img_path[12:-4]+'.jpg')
        # print(img_path)
        # print('D:/data/train/'+ img_path[12:-4]+'.jpg')
    except:
        continue

    # cv2.imwrite('D:/data/training/'+ img_path[12:-4]+'.jpg', img)

    # print('D:/data/training/'+ img_path[12:-4]+'.jpg')

for i in range(n_valid):

    x = len(files)

    try:
        r_label = files.pop(random.randint(0,x-1))
        line_list = r_label.split('/t')
        labeling_valid_f.write(r_label)
        img_path = line_list[0]
        image_path = img_path.split('\t')
        # img = cv2.imread(img_path)

        shutil.move(image_path[0], 'D:/data/valid/'+ image_path[0][12:])
        # shutil.move(img_path, valid_dir+ img_path[12:-4]+'.jpg')

    except:
        continue

    # cv2.imwrite('D:/data/validation/'+ img_path[12:-4]+'.jpg', img)


    
#     valid =labeling_valid_f.readlines()
#     duplication = False

#     for line in valid:#
#         if line.strip('/n') == randomLine:##중복 데이터 검출???#
#             duplication = True#
#             break#
#     # if randomLine not in valid:
#     if not duplication:
#         labeling_valid_f = open('D:/label_valid.txt', 'a', encoding='utf-8')
#         labeling_valid_f.write(randomLine+'/n')
#         count+=1
#     if count == n_valid:
#         break


# labeling_valid_f = open('D:/label_valid.txt', 'r', encoding='utf-8')
# valid = labeling_valid_f.readlines()


# count =0
# duplication = False
# for randomLine in files:
#     duplication = False


#     for line in valid:
#         if line == randomLine:##중복 데이터 검출???
#             duplication = True
#             break


#     if not duplication:
#         labeling_train_f.write(randomLine)
        
#         count+=1
#     if count == n_train:
#         break




# ##################################################################### label.txt 8:2 비율로 나누기 끝 ##################################################################################
# # import os
# # import cv2
# # import shutil

# # list = []
# # src = 'D:/OCR_clop/'
# # dir = 'D:/valid/'


# # for i in os.listdir('D:/OCR_clop/'):
# #     path = 'D:/OCR_clop/' + i
# #     # print(path)
    
# #     # img = cv2.imread(path, 0)
# #     # list.append(path)
# #     # print(list) # ['D:/OCR_clop/00110011001_0.jpg']

# # with open('D:/label_valid.txt', 'r', encoding='utf-8') as f:
# #     files_valid = f.readlines()
# #     # print(files_valid)

# #     # with open('D:/label_train.txt', 'r', encoding='utf-8') as f:
# #     #     files_train = f.readlines()

# #     # if files_valid == path:
# #     #     shutil.move(src + img, dir + img) # i말고

# #     if i in path:
# #         # print(i)
# #         # print(path)
# #         shutil.move(src + i, dir + i) # i말고

