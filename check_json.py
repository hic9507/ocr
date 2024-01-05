import json
import matplotlib.pyplot as plt
import cv2

file = json.load(open('D:/OCR/Training/label_Training_printed/001/00110011001.json', encoding='UTF-8'))
file.keys() #dict_keys(['info', 'images', 'annotations', 'licenses'])
print(file['info']) #{'name': 'Text in the wild Dataset', 'date_created': '2019-10-14 04:31:48'}
print(file.keys())
#print(type(file['images'])) #list

print("file.keys는")
print(file.keys())

print('images의 type은')
print(type(file['image']))

print('file의 정보는')
print(file['info'])

print('---------------')
print(file['image'])

print('annotation 정보')
print(file['text'])

print('license 정보')
print(file['license'])

#file['images'][0]['type'] == 'book' # True
#goods = [f for f in file['images'] if f['type']=='product']
#len(goods)
#print(len(goods)) #26358
#print(goods[0])

#annotation = [a for a in file['annotations'] if a['image_id'] == goods[0]['id'] and a['attributes']['class']=='word']
#print(annotation)

# img = cv2.imread('D:/korean/04.Text in the wild/Goods/'+goods[0]['file_name'])
# plt.imshow(img)
# plt.show()
# print(file.keys())
# print(file['info'])
#print(file['images'])