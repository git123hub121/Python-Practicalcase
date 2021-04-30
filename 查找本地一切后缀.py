import os
import fnmatch
# 查找目录
rootPath = input("请输入你要查询的路径：(默认输入 / 查找全盘) 如 C:/ D:/ E:/"+"\n")
#rootPath = 'D:/'    #默认是    /   也可以写成其他 C:/ D:/ E:/ 等等
# 匹配参数
pattern = '*.'+input("请输入你要查询的文件类型，输入格式为：文件后缀名 如后缀 jpg mp4 mp3  py "+"\n")
#pattern = '*.docx'   #随意修改后缀即可   如jpg mp4 mp3  py 等等
count = 0
for root, dirs, files in os.walk(rootPath):# 
  # 如果匹配输出文件名
  for filename in fnmatch.filter(files, pattern):
    count += 1
    print('第 {} 条：'.format(count),os.path.join(root, filename))#
print('你查询的是{}区域的.{}文件,总记录数为：{} '.format(rootPath,pattern,count))
#很实用，那就改成程序

# import os
# import fnmatch
# # 查找目录
# rootPath = '/'
# # 匹配参数
# pattern = '*.mp3'

# for root, dirs, files in os.walk(rootPath):
#   # 如果匹配输出文件名
#   for filename in fnmatch.filter(files, pattern):
#     print(os.path.join(root, filename))