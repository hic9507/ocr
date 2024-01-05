# import json
# import random
# import os
# from tqdm import tqdm
#
# # htr / ocr
# data_type = 'htr'
# # handwriting_data_info1.json / printed_data_info.json
# labeling_filename = 'handwriting_data_info_clean.json'
#
# ## Check Json File
# file = json.load(open(f'D:/korean/htr/handwriting_data_info_clean.json', encoding='UTF8'))
#
# ## Separate dataset - train, validation, test
# image_files = os.listdir(f'D:/korean/htr/2_sentence')
# total = len(image_files)
# print("------------------------------------------------------------")
# print(total)
#
# random.shuffle(image_files)
#
# n_train = int(len(image_files) * 0.7)
# n_validation = int(len(image_files) * 0.15)
# n_test = int(len(image_files) * 0.15)
#
# print("*************************************************************")
# print(n_train, n_validation, n_test)
#
# train_files = image_files[:n_train]
# validation_files = image_files[n_train:n_train+n_validation]
# test_files = image_files[-n_test:]
#
# ## Separate image id - train, validation, test
# train_img_ids = {}
# validation_img_ids = {}
# test_img_ids = {}
#
# for image in file['images']: # {filename}: {image id}
#   if image['file_name'] in train_files:
#     train_img_ids[image['file_name']] = image['id']
#   elif image['file_name'] in validation_files:
#     validation_img_ids[image['file_name']] = image['id']
#   elif image['file_name'] in test_files:
#     test_img_ids[image['file_name']] = image['id']
#
# ## Annotations - train, validation, test
# train_annotations = {f:[] for f in train_img_ids.keys()} # {image id}: []
# validation_annotations = {f:[] for f in validation_img_ids.keys()}
# test_annotations = {f:[] for f in test_img_ids.keys()}
#
# train_ids_img = {train_img_ids[id_]:id_ for id_ in train_img_ids}
# validation_ids_img = {validation_img_ids[id_]:id_ for id_ in validation_img_ids}
# test_ids_img = {test_img_ids[id_]:id_ for id_ in test_img_ids}
#
# for idx, annotation in enumerate(file['annotations']):
#   if idx % 5000 == 0:
#     print(idx,'/',len(file['annotations']),'processed')
#   if annotation['image_id'] in train_ids_img:
#     train_annotations[train_ids_img[annotation['image_id']]].append(annotation)
#   elif annotation['image_id'] in validation_ids_img:
#     validation_annotations[validation_ids_img[annotation['image_id']]].append(annotation)
#   elif annotation['image_id'] in test_ids_img:
#     test_annotations[test_ids_img[annotation['image_id']]].append(annotation)
#
# ## Write json files
# with open(f'train_annotation.json', 'w') as file:
#   json.dump(train_annotations, file)
# with open(f'validation_annotation.json', 'w') as file:
#   json.dump(validation_annotations, file)
# with open(f'test_annotation.json', 'w') as file:
#   json.dump(test_annotations, file)
#
# ## Make gt_xxx.txt files
# data_root_path = f'D:/korean/htr/2_sentence'
# save_root_path = f'C:/Users/user/.conda/envs/craft-pytorch/deep-text-recognition-benchmark/data_printed'
#
# obj_list = ['test', 'train', 'validation']
# for obj in obj_list:
#   total_annotations = json.load(open(f'./{obj}_annotation.json'))
#   gt_file = open(f'{save_root_path}gt_{obj}.txt', 'w')
#   for file_name in tqdm(total_annotations):
#     annotations = total_annotations[file_name]
#     for idx, annotation in enumerate(annotations):
#       text = annotation['text']
#       gt_file.write(f'{obj}/{file_name}\t{text}')
# #
# # import json
# # import random
# # import os
# # from tqdm import tqdm
# #
# # # htr / ocr
# # data_type = 'htr'
# # # handwriting_data_info1.json / printed_data_info.json
# # labeling_filename = 'handwriting_data_info1.json'
# #
# # ## Check Json File
# # file = json.load(open(f'./kor_dataset/aihub_data/{data_type}/{labeling_filename}'))
# #
# # ## Separate dataset - train, validation, test
# # image_files = os.listdir(f'./kor_dataset/aihub_data/{data_type}/images/')
# # total = len(image_files)
# #
# # random.shuffle(image_files)
# #
# # n_train = int(len(image_files) * 0.7)
# # n_validation = int(len(image_files) * 0.15)
# # n_test = int(len(image_files) * 0.15)
# #
# # print(n_train, n_validation, n_test)
# #
# # train_files = image_files[:n_train]
# # validation_files = image_files[n_train:n_train+n_validation]
# # test_files = image_files[-n_test:]
# #
# # ## Separate image id - train, validation, test
# # train_img_ids = {}
# # validation_img_ids = {}
# # test_img_ids = {}
# #
# # for image in file['images']: # {filename}: {image id}
# #   if image['file_name'] in train_files:
# #     train_img_ids[image['file_name']] = image['id']
# #   elif image['file_name'] in validation_files:
# #     validation_img_ids[image['file_name']] = image['id']
# #   elif image['file_name'] in test_files:
# #     test_img_ids[image['file_name']] = image['id']
# #
# # ## Annotations - train, validation, test
# # train_annotations = {f:[] for f in train_img_ids.keys()} # {image id}: []
# # validation_annotations = {f:[] for f in validation_img_ids.keys()}
# # test_annotations = {f:[] for f in test_img_ids.keys()}
# #
# # train_ids_img = {train_img_ids[id_]:id_ for id_ in train_img_ids}
# # validation_ids_img = {validation_img_ids[id_]:id_ for id_ in validation_img_ids}
# # test_ids_img = {test_img_ids[id_]:id_ for id_ in test_img_ids}
# #
# # for idx, annotation in enumerate(file['annotations']):
# #   if idx % 5000 == 0:
# #     print(idx,'/',len(file['annotations']),'processed')
# #   if annotation['image_id'] in train_ids_img:
# #     train_annotations[train_ids_img[annotation['image_id']]].append(annotation)
# #   elif annotation['image_id'] in validation_ids_img:
# #     validation_annotations[validation_ids_img[annotation['image_id']]].append(annotation)
# #   elif annotation['image_id'] in test_ids_img:
# #     test_annotations[test_ids_img[annotation['image_id']]].append(annotation)
# #
# # ## Write json files
# # with open(f'{data_type}_train_annotation.json', 'w') as file:
# #   json.dump(train_annotations, file)
# # with open(f'{data_type}_validation_annotation.json', 'w') as file:
# #   json.dump(validation_annotations, file)
# # with open(f'{data_type}_test_annotation.json', 'w') as file:
# #   json.dump(test_annotations, file)
# #
# # ## Make gt_xxx.txt files
# # data_root_path = f'./kor_dataset/aihub_data/{data_type}/images/'
# # save_root_path = f'./deep-text-recognition-benchmark/{data_type}_data/'
# #
# # obj_list = ['test', 'train', 'validation']
# # for obj in obj_list:
# #   total_annotations = json.load(open(f'./{data_type}_{obj}_annotation.json'))
# #   gt_file = open(f'{save_root_path}gt_{obj}.txt', 'w')
# #   for file_name in tqdm(total_annotations):
# #     annotations = total_annotations[file_name]
# #     for idx, annotation in enumerate(annotations):
# #       text = annotation['text']
# #       gt_file.write(f'{obj}/{file_name}\t{text}')

# import json
# import os
# import cv2
# import matplotlib.pyplot as plt
# from tqdm import tqdm
#
# ## aihub 데이터 annotation을 읽어서 단어 단위로 잘라서 data에 저장하기
#
# data_root_path = 'D:/new/ori/001/'
# save_root_path = 'D:/new/ori/001/002/'
#
# test_annotations = json.load(open('C:/Users/user/anaconda3/envs/craft-pytorch/deep-text-recognition-benchmark/test_gt.json'))
# gt_file = open(save_root_path + 'gt_test.txt', 'w')
# for file_name in tqdm(test_annotations):
#   annotations = test_annotations[file_name]
#   image = cv2.imread(data_root_path + file_name)
#   for idx, annotation in enumerate(annotations):
#     x, y, w, h = annotation['bbox']
#     if x <= 0 or y <= 0 or w <= 0 or h <= 0:
#       continue
#     text = annotation['text']
#     crop_img = image[y:y + h, x:x + w]
#     crop_file_name = file_name[:-4] + '_{:03}.jpg'.format(idx + 1)
#     cv2.imwrite(save_root_path + 'test/' + crop_file_name, crop_img)
#     gt_file.write("test/{}\t{}\n".format(crop_file_name, text))
#
# validation_annotations = json.load(open('./validation_annotation.json'))
# gt_file = open(save_root_path + 'gt_validation.txt', 'w')
# for file_name in tqdm(validation_annotations):
#   annotations = validation_annotations[file_name]
#   image = cv2.imread(data_root_path + file_name)
#   for idx, annotation in enumerate(annotations):
#     x, y, w, h = annotation['bbox']
#     if x <= 0 or y <= 0 or w <= 0 or h <= 0:
#       continue
#     text = annotation['text']
#     crop_img = image[y:y + h, x:x + w]
#     crop_file_name = file_name[:-4] + '_{:03}.jpg'.format(idx + 1)
#     cv2.imwrite(save_root_path + 'validation/' + crop_file_name, crop_img)
#     gt_file.write("validation/{}\t{}\n".format(crop_file_name, text))
#
# train_annotations = json.load(open('./train_annotation.json'))
# gt_file = open(save_root_path + 'gt_train.txt', 'w')
# for file_name in tqdm(train_annotations):
#   annotations = train_annotations[file_name]
#   image = cv2.imread(data_root_path + file_name)
#   for idx, annotation in enumerate(annotations):
#     x, y, w, h = annotation['bbox']
#     if x <= 0 or y <= 0 or w <= 0 or h <= 0:
#       continue
#     text = annotation['text']
#     crop_img = image[y:y + h, x:x + w]
#     crop_file_name = file_name[:-4] + '_{:03}.jpg'.format(idx + 1)
#     cv2.imwrite(save_root_path + 'train/' + crop_file_name, crop_img)
#     gt_file.write("train/{}\t{}\n".format(crop_file_name, text)).

import random
import os
import json

base_label_path = 'D:/OCR/Training/label_Training_printed/'
base_image_path = 'D:/OCR_clop/'

# ocr_files = os.listdir('D:/OCR_clop/')
ocr_files = os.listdir(base_image_path)
# print(len(ocr_good_files)) # 37220

random.shuffle(ocr_files)

n_train = int(len(ocr_files) * 0.8)
n_validation = int(len(ocr_files) * 0.2)
# n_test = int(len(ocr_good_files) * 0.2)

# print(n_train, n_validation, n_test) # 26054 5583 5583

train_files = ocr_files[:n_train]
validation_files = ocr_files[n_train: n_train+n_validation]
# print(train_files)#
# test_files = ocr_good_files[-n_test:]

## train/validation/test 이미지들에 해당하는 id 값을 저장

train_img_ids = {}
validation_img_ids = {}
# test_img_ids = {}

################################## json 파일 읽어오기
for q in os.listdir(base_label_path):
    num_folder = q
    # print(num_folder) # 001~050
    for w in os.listdir(base_label_path + num_folder):
        label_file_name = w
         
        # print(label_file_name) ### 00110011001.json~05010103040.json

        ### 모든 폴더에 있는 json 파일 다 읽어와서 f에 저장
        f = (open(base_label_path + num_folder + '/' + label_file_name, 'r', encoding='utf-8'))
        file_json = json.load(f)

        for id in range(len(file_json['text']['word'])):     
            bbox = file_json['text']['word'][id]['wordbox']

        # 이미지 이름 가져오기
            labeling = file_json['image']['file_name']
        # 이미지의 한 단어 가져오기
            value = file_json['text']['word'][id]['value']
            


            for image in file_json:
                if value in train_files:
                    
                    train_img_ids[file_json['word']] = labeling
                elif value in validation_files:
                    validation_img_ids[file_json['word']] = labeling
        

## train/validation/test 이미지들에 해당하는 annotation 들을 저장

train_annotations = {f:[] for f in train_img_ids.keys()}
validation_annotations = {f:[] for f in validation_img_ids.keys()}
# test_annotations = {f:[] for f in test_img_ids.keys()}

train_ids_img = {train_img_ids[id_]:id_ for id_ in train_img_ids}
validation_ids_img = {validation_img_ids[id_]:id_ for id_ in validation_img_ids}
# test_ids_img = {test_img_ids[id_]:id_ for id_ in test_img_ids}

for idx, annotation in enumerate(file_json['annotations']):
    if idx % 5000 == 0:
        print(idx,'/',len(file_json['annotations']),'processed')
    if annotation['text']['word'] != 'word':
        continue
    if annotation['image_id'] in train_ids_img:
        train_annotations[train_ids_img[annotation['image_id']]].append(annotation)
    elif annotation['image_id'] in validation_ids_img:
        validation_annotations[validation_ids_img[annotation['image_id']]].append(annotation)
    # elif annotation['image_id'] in test_ids_img:
    #     test_annotations[test_ids_img[annotation['image_id']]].append(annotation)

with open('train_annotation.json', 'w') as file_json:
    json.dump(train_annotations, file_json)
with open('validation_annotation.json', 'w') as file_json:
    json.dump(validation_annotations, file_json)
# with open('test_annotation.json', 'w') as file_json:
#     json.dump(test_annotations, file_json)