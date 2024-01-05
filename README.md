# OCR
## git clone https://github.com/clovaai/deep-text-recognition-benchmark.git
위 주소를 참고했음.

#### check_json.py
json 파일을 읽어와서 해당하는 값들 확인

#### crop2.py, cropping.py, crop_and_save.py
json 파일 읽어와서 필요 좌표 읽고 이미지 crop 후 저장

#### make.py, make(2).py, make_txt.py, make_data.py
txt 파일 읽어와서 데이터셋 비율 나누고 원하는대로 다시 작성

#### move_file.py, get_images.py
메모장 파일 읽어서 원하는 경로로 이동

#### get_images.py
이미지 데이터셋 별로 나누고 경로 읽어서 이동

#### dataset_split.py
데이터셋 비율 별로 이미지 읽고 경로 읽어서 이동
