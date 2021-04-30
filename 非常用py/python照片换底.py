#   文章链接    https://mp.weixin.qq.com/s/NG7KT9awZg7G2x6ZeeQnnA

#   读取图片并显示

# import cv2
# import numpy as np
# # 读取照片
# img=cv2.imread('640.jpg')
#
# # 显示图像
# cv2.imshow('img',img)
#
# # 窗口等待的命令，0表示无限等待
# cv2.waitKey(0)

#   图片缩放

# import cv2
# import numpy as np
# # 读取照片
# img=cv2.imread('640.jpg')
#
# # 图像缩放
# img = cv2.resize(img,None,fx=0.5,fy=0.5)
# rows,cols,channels = img.shape
# print(rows,cols,channels)

# 显示图像
# cv2.imshow('img',img)
#
# # 窗口等待的命令，0表示无限等待
# cv2.waitKey(0)

#   将图片转换为灰度图像

# import cv2
# import numpy as np
# # 读取照片
# img=cv2.imread('640.jpg')
#
# # 图像缩放
# img = cv2.resize(img,None,fx=0.5,fy=0.5)
# rows,cols,channels = img.shape
# print(rows,cols,channels)
# cv2.imshow('img',img)
#
# # 图片转换为二值化图
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#
# # 显示图像
# cv2.imshow('hsv',hsv)
#
# # 窗口等待的命令，0表示无限等待
# cv2.waitKey(0)

#   将图片进行二值化处理

# import cv2
# import numpy as np
# # 读取照片
# img=cv2.imread('640.jpg')
#
# # 图像缩放
# img = cv2.resize(img,None,fx=0.5,fy=0.5)
# rows,cols,channels = img.shape
# print(rows,cols,channels)
# cv2.imshow('img',img)
#
# # 图片转换为灰度图
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv',hsv)
#
# # 图片的二值化处理
# lower_blue = np.array([90,70,70])
# upper_blue = np.array([110,255,255])
# mask = cv2.inRange(hsv, lower_blue, upper_blue)
#
#
# # 显示图像
# cv2.imshow('mask',mask)
#
# # 窗口等待的命令，0表示无限等待
# cv2.waitKey(0)

#   图象的腐蚀和膨胀

# import cv2
# import numpy as np
# # 读取照片
# img=cv2.imread('640.jpg')
#
# # 图像缩放
# img = cv2.resize(img,None,fx=0.5,fy=0.5)
# rows,cols,channels = img.shape
# print(rows,cols,channels)
# cv2.imshow('img',img)
#
# # 图片转换为灰度图
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv',hsv)
#
# # 图片的二值化处理
# lower_blue=np.array([90,70,70])
# upper_blue=np.array([110,255,255])
# mask = cv2.inRange(hsv, lower_blue, upper_blue)
#
#
# #腐蚀膨胀
# erode=cv2.erode(mask,None,iterations=1)
# cv2.imshow('erode',erode)
#
# dilate=cv2.dilate(erode,None,iterations=1)
# cv2.imshow('dilate',dilate)
#
#
# # 窗口等待的命令，0表示无限等待
# cv2.waitKey(0)

#   遍历每个像素点进行颜色替换——最终效果！

import cv2
import numpy as np
# 读取照片
img=cv2.imread('640.jpg')

# 图像缩放
img = cv2.resize(img,None,fx=0.5,fy=0.5)
rows,cols,channels = img.shape
print(rows,cols,channels)
cv2.imshow('img',img)

# 图片转换为灰度图
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)

# 图片的二值化处理
lower_blue=np.array([90,70,70])
upper_blue=np.array([110,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)


#腐蚀膨胀
erode=cv2.erode(mask,None,iterations=1)
cv2.imshow('erode',erode)

dilate=cv2.dilate(erode,None,iterations=1)
cv2.imshow('dilate',dilate)

#遍历每个像素点，进行颜色的替换
for i in range(rows):
  for j in range(cols):
    if erode[i,j]==255: # 像素点为255表示的是白色，我们就是要将白色处的像素点，替换为红色
      img[i,j]=(0,0,255) # 此处替换颜色，为BGR通道，不是RGB通道
cv2.imshow('res',img)

# 窗口等待的命令，0表示无限等待
cv2.waitKey(0)

#   但是转换后明显有瑕疵！还是用ps好！