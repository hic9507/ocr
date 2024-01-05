import random
import os
import json
import tqdm
import cv2

file = json.load(open('D:/korean/04.Text in the wild/textinthewild_data_info.json', encoding='UTF8'))
file.keys()


ocr_good_files = os.listdir('D:/korean/04.Text in the wild/Traffic_Sign/')
len(ocr_good_files) # 37220, 47304
print(len(ocr_good_files))

random.shuffle(ocr_good_files)

n_train = int(len(ocr_good_files) * 0.7)
n_validation = int(len(ocr_good_files) * 0.15)
n_test = int(len(ocr_good_files) * 0.15)

print(n_train, n_validation, n_test) # 26054 5583 5583, 28212 6045 6045

train_files = ocr_good_files[:n_train]
validation_files = ocr_good_files[n_train: n_train+n_validation]
test_files = ocr_good_files[-n_test:]

## train/validation/test 이미지들에 해당하는 id 값을 저장

train_img_ids = {}
validation_img_ids = {}
test_img_ids = {}

for image in file['images']:
    if image['file_name'] in train_files:
        train_img_ids[image['file_name']] = image['id']
        #print("train")
    elif image['file_name'] in validation_files:
        validation_img_ids[image['file_name']] = image['id']
        #print("val")
    elif image['file_name'] in test_files:
        test_img_ids[image['file_name']] = image['id']
        #print("test")

## train/validation/test 이미지들에 해당하는 annotation 들을 저장

train_annotations = {f:[] for f in train_img_ids.keys()}
validation_annotations = {f:[] for f in validation_img_ids.keys()}
test_annotations = {f:[] for f in test_img_ids.keys()}

train_ids_img = {train_img_ids[id_]:id_ for id_ in train_img_ids}
validation_ids_img = {validation_img_ids[id_]:id_ for id_ in validation_img_ids}
test_ids_img = {test_img_ids[id_]:id_ for id_ in test_img_ids}

for idx, annotation in enumerate(file['annotations']):
    if idx % 5000 == 0:
        print(idx,'/',len(file['annotations']),'processed')
    # if annotation['attributes']['type'] != '문장':
    if annotation['attributes']['class'] != 'word':
        continue
    if annotation['image_id'] in train_ids_img:
        train_annotations[train_ids_img[annotation['image_id']]].append(annotation)
    elif annotation['image_id'] in validation_ids_img:
        validation_annotations[validation_ids_img[annotation['image_id']]].append(annotation)
    elif annotation['image_id'] in test_ids_img:
        test_annotations[test_ids_img[annotation['image_id']]].append(annotation)

with open('train_annotation.json', 'w') as file:
    json.dump(train_annotations, file)
with open('validation_annotation.json', 'w') as file:
    json.dump(validation_annotations, file)
with open('test_annotation.json', 'w') as file:
    json.dump(test_annotations, file)


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

# test_annotations = json.load(open('./test_annotation.json'))
# gt_file = open(save_root_path + 'gt_test.txt', 'w')
# for file_name in tqdm(test_annotations):
#     annotations = test_annotations[file_name]
#     image = cv2.imread(data_root_path + file_name)