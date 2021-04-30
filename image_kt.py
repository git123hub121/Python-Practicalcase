import os
import paddlehub as hub

# 加载模型
humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')
base_dir = os.path.abspath(os.path.dirname(__file__))

# 获取当前文件目录
path = os.path.join(base_dir,'source/')

# 获取文件列表
files = [path + i for i in os.listdir(path)]
print(files)
# 抠图
results = humanseg.segmentation(data={'image': files})
for result in results:
    print(result)

    #文件目不能是中文才行
    #一键抠图成功！