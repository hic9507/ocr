import shutil
import time
data_root_path = 'D:/korean/htr/2_sentence/'
save_root_path = 'C:/Users/user/.conda/envs/craft-pytorch/deep-text-recognition-benchmark/data_printed/'
#save_root_path = ''
print(save_root_path)

# copy images from dataset directory to current directory
# shutil.copytree(data_root_path, save_root_path)

# separate dataset : train, validation, test
obj_list = ['train', 'test', 'validation']
for obj in obj_list:
  with open(f'data_printedgt_{obj}.txt', 'r') as f:
    lines = f.readlines()
    lines = lines[0].split('\t')

    for line in lines:
      print(line)
      # time.sleep(20000)
      file_path = line.split('.png')[0]
      # print(file_path)
      file_name = file_path.split('/')[1] + '.png'
      # print(file_name)
      # print(save_root_path+file_name)
      res = shutil.move(save_root_path+file_name, f'./data_printed/{obj}/')