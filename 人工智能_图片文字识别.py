import requests
from aip import AipOcr

# 账户信息
APP_ID = '20102353'
API_KEY = 'GINgFaT9BXGF6QSUhKjVlPDG'
SECRET_KEY = 'COChejD8vCTn9IqGFCg1mmUGrd0ur2tE'

# 生成一个人工智能识别对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY )

# 请求获取一个图片内容
image = requests.get("https://hbimg-other.huabanimg.com/340b9a993c75039c3a24f6ac6577121e0178fe4e1f5bc_fw236/format/webp").content

# 请求识别图像
res = client.basicAccurate(image)

# 打印并输出图片里的文字
if 'words_result' in res.keys():
  for item in res['words_result']:
    print(item['words'])

    #真的流弊