

list = []
src = 'D:/OCR_clop/'
dir = 'D:/valid/'

for i in os.listdir('D:/OCR_clop/'):
    path = 'D:/OCR_clop/' + i
    # print(len(i))

    img = cv2.imread(path, 0)
    # list.append(path)
    # print(list) # ['D:/OCR_clop/00110011001_0.jpg']

    with open('D:/label_valid.txt', 'r', encoding='utf-8') as f:
        files_valid = f.readlines()
        # print(files_valid)

    # with open('D:/label_train.txt', 'r', encoding='utf-8') as f:
    #     files_train = f.readlines()

    if files_valid == path:
        shutil.move(src + img, dir + img)  # i말고