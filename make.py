import os

# F = open('C:/Users/user/Desktop/label1.txt', 'w', encoding='utf-8')

with open('C:/Users/user/Desktop/label.txt', 'r', encoding='utf-8')as f:
    labeling_f = f.readlines()

with open('C:/Users/user/Desktop/label1114.txt', 'r', encoding='utf-8')as f:
    train_f = f.readlines()

# print(labeling_f)
# print(train_f)

if train_f in labeling_f:
    print('1')
else:
    print('0')

# for i in labeling_f:
#     if train_f in labeling_f:
#         del i
        # F.write('D:/OCR_clop/' + labeling[:-4] + '_' +str(count)+'.jpg' +'\t' + value +'\n')
        # F.write(i)
