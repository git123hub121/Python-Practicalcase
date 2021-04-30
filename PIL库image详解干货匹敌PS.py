#实例一：   GIF文件图像提取
# from PIL import Image
# im = Image.open('1.gif')#读入一个gif文件
# try:
#     im.save('picframe {:02d}.png'.format(im.tell()))
#     while True:
#         im.seek(im.tell()+1)
#     im.save('picframe {:02d}.png'.format(im.tell()))
# except:
#     print("处理结束")

#实例二    缩略图 图片尺寸
# im.thumbnall((120,120))
# im.save("p","jpg")

#实例三 略，感觉不是很有关系了！
