'''
本源码来自公众号【菜鸟学Python】，目前原创了近400篇趣味的Python干货案例
累计有30万Python爱好者关注，更多原创案例源码，欢迎来公众号着我们。
'''
import os
import cv2
import numpy as np
from tkinter import *
from tkinter.messagebox import showerror, showinfo

class JiuGongGe(object):
    def __init__(self):
        self.root = Tk()  # 创建Tk对象
        self.root.title("九宫格转换器")  # 设置窗口标题
        self.h, self.w = 480, 640
        self.root.geometry("{}x{}".format(self.w, self.h))  # 设置窗口尺寸

        self.title = Label(self.root, text="九宫格转换器")  # 标签
        self.title.place(x = int(self.w/2),y = 10,anchor = CENTER)

        self.label1 = Label(self.root, text="请输入转换图片地址")  # 标签
        self.label1.place(x=0, y=30, anchor=NW)
        self.picttext = Entry(highlightcolor='red', highlightthickness=1, width=50)  # 创建文本框
        self.picttext.place(x=0, y=60, anchor=NW)

        self.label2 = Label(self.root, text="请输入转换后图片保存的文件夹")  # 标签
        self.label2.place(x=0, y=90, anchor=NW)
        self.savetext = Entry(highlightcolor='red', highlightthickness=1, width=50)  # 创建文本框
        self.savetext.place(x=0, y=120, anchor=NW)
        button = Button(self.root, text="开始转换",command=self.Run)  # command绑定获取文本框内容方法
        button.place(x=int(self.w / 2), y=300, anchor=NW)
        self.root.mainloop()  # 进入主循

    def Run(self):
        picPath = self.picttext.get()
        savePath = self.savetext.get()

        if not os.path.exists(savePath):
            os.makedirs(savePath)
        try:
            img = cv2.imread(picPath)
            height, width = img.shape[:2]
            # 开始准备将图片扩展到正方形，以长边为基准
            bigLine = max(height, width)
            newImg = np.zeros([bigLine, bigLine, 3], np.uint8)+255
            if height > width:
                edge = (bigLine - width) // 2
                newImg[:, edge:width+edge,:] = img
            else:
                edge = (bigLine - height) // 2
                newImg[edge:height + edge,:, :] = img
            subHeight, subWidth = int(bigLine / 3), int(bigLine / 3)
        except  AttributeError:
            showerror("提示", "图片路径错误，请重新检查输入！")
            return
        for i in range(3):
            for j in range(3):
                if(i < 2):
                    if j < 2:
                        tempImg = newImg[i * subHeight:(i + 1) * subHeight, j * subWidth:(j + 1) * subWidth, :]
                    else:
                        tempImg = newImg[i * subHeight:(i + 1) * subHeight, j * subWidth:, :]

                else:
                    if j < 2:
                        tempImg = newImg[i * subHeight:, j * subWidth:(j + 1) * subWidth, :]
                    else:
                        tempImg = newImg[i * subHeight:, j * subWidth:, :]
                cv2.imwrite(savePath + "/{}.jpg".format(i * 3 + j), tempImg)

        showinfo("提示", "转换已经完成！")



if __name__ == '__main__':
    JiuGongGe()


