##################################################################### label.txt 8:2 비율로 나누기 시작 ##################################################################################
import os
import cv2
import random
import shutil
import re

labeling_total_f = open('D:/label.txt', 'r', encoding='utf-8')
labeling_train_f = open('D:/data/train_gt.txt', 'r', encoding='utf-8')
labeling_valid_f = open('D:/data/valid_gt.txt', 'r', encoding='utf-8')

# a = open('C:/Users/user/Desktop/test/label.txt', 'r', encoding='utf-8')
# # print(a)
# b = a.split('\t')

# with open('C:/Users/user/Desktop/test/label.txt', 'r', encoding='utf-8')as f:
#     a = f.readlines() ############
with open('C:/Users/user/Desktop/label1114.txt', 'r', encoding='utf-8')as f:
    a = f.readlines()

# for line in a:
#     b = line.split('\t')[0]
#     c = line.split('\t')[1]
#     print(b, c)
#     train_f = f.readlines()
#     print(len(train_f[0]))
# for line in train_f:
#     a = line.split('\t')[0]

labeling_f = open('C:/Users/user/Desktop/1118.txt', 'w', encoding='utf-8')


Settotal = set(labeling_total_f)
Settrain = set(labeling_train_f) 
Setvalid = set(labeling_valid_f)
a = Settotal
b = Settrain
c = Setvalid
d = Settotal - (Settrain | Setvalid)
l = list(d)
print(l, file=labeling_f)
# e = Settotal - Setvalid


# print(l, file=labeling_f)

# with open('C:/Users/user/Desktop/label1114.txt', 'r', encoding='utf-8')as f:############
#     train_f = f.readlines()
#     print(len(train_f[0]))
# for line in train_f:
#     a = line.split('\t')[0]
# #b = re.split(r"\t+", a.rstrip('\t'))
# #b = a.split('\t')
#     print(a)###########################################################
# ww_f = open('C:/Users/user/Desktop/label2.txt', 'a', encoding='utf-8')
# print(l + '\n')
# print(train_f)
# f = l.readline()
# labeling_f.write(Settotal - Settrain)
# print(c, file=labeling_f)
# print(f)
# print(l, file=labeling_f)



# with open('D:/test/total.txt', 'r', encoding='utf-8') as f:
#     label = f.readlines()
# # print(label[0])
# list = []
# list1 = []
# list.append(label)
# # print(list)
# for j in list:
#     for i in os.listdir('D:/test/train/'):
#         list1.append(i)
#         # print(list1)
#         if list1 in list:
#             print(list1)
#         else:
#             print('no')





# n_samples = len(files) # 9546600

# n_train = int(n_samples * 0.8)
# n_valid = int(n_samples * 0.2)

# print(n_samples, n_train, n_valid)
# print('================================================================')

# for _ in range(n_train):

#     x = len(files)

#     try:
#         r_label = files.pop(random.randint(0,x-1))
#         # print(r_label)
#         line_list = r_label.split('\t')
#         labeling_train_f.write(r_label)
#         img_path = line_list[0]
#         # print('img_path: ', img_path)
#         # print('================================================================')
#         # print('line_list: ', line_list)
#         # print('================================================================')
#         # print('line_list[0]: ', line_list[0])
#         # print('================================================================')
#         # print(img_path[14:])
#         shutil.move(img_path, 'D:/test/train/'+ img_path[14:])
#     except:
#         continue


# for i in range(n_valid):

#     x = len(files)

#     try:
#         r_label = files.pop(random.randint(0,x-1))
#         line_list = r_label.split('\t')
#         labeling_valid_f.write(r_label)
#         img_path = line_list[0]

#         shutil.move(img_path, 'D:/test/valid/'+ img_path[14:])
        
#     except:
#         continue
