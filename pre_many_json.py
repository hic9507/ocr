import json
import pandas as pd
import io, os
from PIL import Image
import cv2
import glob

base_label_path = 'D:/OCR/Training/label_Training_printed/001/'
base_image_path = 'D:/OCR/Training/ori_Training_printed/from/001/'
for filename in os.listdir(base_label_path):
    if filename.endswith('.json'):
        files = filename