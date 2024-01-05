import json
import pandas as pd
import io, os
from PIL import Image
import cv2
import glob

path = 'D:/OCR/Training/label_Training_printed/001/'
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('.json')] ## 파일명 끝이 .csv인 경우

## csv 파일들을 DataFrame으로 불러와서 concat

df = pd.DataFrame()
for i in file_list_py:
    data = pd.read_json(path + i)
    df = pd.concat([df, data])

df = df.reset_index(drop=True)

## json 파일들을 DataFrame으로 불러오기

import json

dict_list = []
for i in file_list_py:
    for line in open((path+i),"r", encoding='utf-8'):
        dict_list.append(json.loads(line))
df = pd.DataFrame(dict_list)