import os
import shutil
import glob
# 设置建立分类总文件夹的路径，这里按自己的实际路径修改
mkdir_path = r'C:\Users\ASUS\Desktop\文件夹分类'
# 设置需要遍历整理的文件夹路径，可以依据自己的实际需求修改
goal_dir = r'C:\Users\ASUS\Desktop\文件'

if not os.path.exists(mkdir_path):
    os.mkdir(mkdir_path)

file_num = 0
dir_num = 0

for file in glob.glob(f'{goal_dir}/**/*', recursive=True):
    if os.path.isfile(file):
        filename = os.path.basename(file)
        if '.' in filename:
            suffix = filename.split('.')[-1]
        else:
            suffix = 'others'
        if not os.path.exists(f'{mkdir_path}/{suffix}'):
            os.mkdir(f'{mkdir_path}/{suffix}')
            dir_num += 1
        shutil.copy(file, f'{mkdir_path}/{suffix}')
        file_num += 1

print(f'整理完成，有{file_num}个文件分类到了{dir_num}个文件夹中')

#文章链接：  https://mp.weixin.qq.com/s/5XLQC__oezzLJdmfh5g8Rw
#确实可行！但是不要乱试