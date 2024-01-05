import os
import cv2
import random

labeling_valid_f = open('D:/zzva.txt', 'a', encoding='utf-8')
labeling_train_f = open('D:/zztr.txt', 'a', encoding='utf-8')

with open('D:/abc.txt', 'r', encoding='utf-8') as f:
    files = f.readlines()

n_samples = len(files) # 9546600

n_train = int(n_samples * 0.8)
n_valid = int(n_samples * 0.2)
print('n_train에 들어갈 숫자의 개수: ', n_train)
print('n_valid에 들어갈 숫자의 개수: ', n_valid)
print('-'*100)

for _ in range(n_train):

    x = len(files)


    r_label = files.pop(random.randint(0,x-1))
    print('train 메모장: ', r_label)


    line_list = r_label.split('\t')
    # print(line_list)


    labeling_train_f.write(r_label)




    img_path = line_list[0]

    # print(img_path)
    # img = cv2.imread(img_path)

    # cv2.imwrite('D:/data/training/'+ img_path[12:-4]+'.jpg', img)

    # print('D:/data/training/'+ img_path[12:-4]+'.jpg')
print('-'*100)
for _ in range(n_valid):

    x = len(files)


    r_label = files.pop(random.randint(0,x-1))
    print('valid 메모장: ', r_label)


    line_list = r_label.split('\t')


    labeling_valid_f.write(r_label)




    img_path = line_list[0]

    # img = cv2.imread(img_path)

    # cv2.imwrite('D:/data/validation/'+ img_path[12:-4], img)