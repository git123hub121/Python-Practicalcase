'''
Author: 你爸爸lzm
Date: 2020-05-31 23:55:45
Notes: 使用built命令快速得到一些常用的snippets,右击py文件可以preview代码
LastEditTime: 2020-12-18 21:12:16
'''
from wordcloud import WordCloud
import numpy as np
# 创建词云对象
font = "C:\\Windows\\Fonts\\STXINGKA.TTF"#词云的中文字体所在路径
wc = WordCloud(font_path = font,#这里要设置，否则中文会乱码
               # background_color="white",
               # contour_width=5,
               # contour_color="lightblue",
               )
wc.generate("喜欢你 还没有爱你，我想以后爱你的那个人是我，我希望以后爱我的人是你 我喜欢的你  这一路上有你——微光")    # 生成词云
wc.to_file('img/歌词评论.png')    # 保存词云

# #高级版
# def wordcloud(self):
#     self.name = input('请输入要生成词云图的文件名称：')

#     def cut(text):
#         wordlist_jieba = jieba.cut(text)
#         space_wordlist = " ".join(wordlist_jieba)
#         return space_wordlist

#     with open('D:/Python/'+self.name + ".txt", encoding="utf-8")as file:
#         text = file.read()
#         text = cut(text)
#         mask_pic = numpy.array(Image.open("D:/Python/img/vscode.jpg"))
#         wordcloud = WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",
#                               collocations=False,
#                               max_words=100,
#                               min_font_size=10,
#                               max_font_size=500,
#                               mask=mask_pic).generate(text)
#         image=wordcloud.to_image()
#         image.show()
#         wordcloud.to_file(self.name + '词云图.png')  # 把词云保存下来
#     print('生成成功！\n')
