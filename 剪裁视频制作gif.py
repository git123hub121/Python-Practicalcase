# import imageio
import imageio_ffmpeg
import PIL

from moviepy import editor
import moviepy.editor as mpy
from moviepy.editor import VideoFileClip
from moviepy.editor import CompositeVideoClip
from moviepy.video.VideoClip import TextClip

#           1

def Base(path="D:/文件/我的编程项目/PHP网页制作/www/video/weiguang.mp4", duration=((0,0,48),(0,0,51)), savepath="C:/Users/Public/Desktop/out3.gif"):
    c = VideoFileClip(path).subclip(duration[0],duration[1]).speedx(0.3).resize(0.5)
    c.write_gif(savepath)
print(Base())
    # 剪裁指定时间内的视频
    #速度降为0.3
    #将剪裁的视频分辨率减少一半

#视频文件的本地路径        2
# 剪辑?分?秒到?分?秒的片段。注意：不使用resize则不会修改清晰度
# 将片段保存为gif图到python的默认路径，可保存到"C:\Users\Administrator\Desktop"
content = mpy.VideoFileClip("D:/文件/我的编程项目/PHP网页制作/www/video/weiguang.mp4")
c1 = content.subclip((0,42),(0,45)).resize((540,480)).speedx(0.5)
c1.write_gif("C:/Users/Public/Desktop/out1.gif")

# #截取想要的部分的小姐姐图像    3
#剪裁指定时间内的视频
#剪裁指定区域内的视频
#速度降为0.5
#将剪裁的视频分辨率减少一半

#3
def SecondLevel(path="D:/文件/我的编程项目/PHP网页制作/www/video/weiguang.mp4",duration=((0,0,45), (0,0,48)),savepath="C:/Users/Public/Desktop/out2.gif",region=(0,0,540,480)):
    video = VideoFileClip(path).subclip(duration[0],duration[1]).crop(x1=region[0],y1=region[1],x2=region[2],y2=region[3]).speedx(0.5).resize(0.5)
    video.write_gif(savepath)
print(SecondLevel())

# #4
# def ThildLevel(path="C:/Users\ASUS\Desktop\文件\旅心网_www\www\\video\weiguang.mp4",duration=((0,0,51), (0,0,54)),savepath="C:\\Users\\ASUS\\Desktop\\out4.gif",region=(0,0,540,480), text="lzm"):
#     video = VideoFileClip(path).subclip(duration[0],duration[1]).crop(x1=region[0],y1=region[1],x2=region[2],y2=region[3]).speedx(0.5).resize(0.5)
#     #创建文字
#     text = TextClip(text, fontsize=20, color='white', interline=25, font="FangSong").set_position(2,1).set_duration(video.duration)
#     compose = CompositeVideoClip([video,text])
#     compose.write_gif(savepath)
# print(ThildLevel()) #需要安装ImageMagick模块