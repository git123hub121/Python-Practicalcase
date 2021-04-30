from MyQR import myqr
myqr.run(
    words='http://www.baidu.com',    # 包含信息
    picture='1.png',            # 背景图片
    colorized=True,            # 是否有颜色，如果为False则为黑白
    save_name='code.png'    # 输出文件名
)
#具体操作：1.将图片路径写入picture  2.words代表你说生成二维码的信息，用手机扫一下即可，如是网址，可以直接访问    3.save_name生成该二维码
#有了第一句就可以直接生成普通二维码了  words='http://www.baidu.com'