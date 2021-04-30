from urllib import request
from tkinter import *

#获取百度翻译IP
url = "http://fanyi.baidu.com"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63"
}
req = request.Request(url,headers=headers)
response = request.urlopen(req)
html = response.read().decode("utf-8") #将网页的信息进行编码，否则会产生乱码
#print(html)
#request.urlretrieve("https://photo.tuchong.com/1732720/f/83757108.jpg","aaa.jpg")

#设计界面
if __name__ == "__main__":
    root = Tk()
    root.title("属于你的翻译器")
    root['width'] = 250
    root['height'] = 130
    Label(root,text='输入要翻译的内容：',width=20).place(x=1,y=1)#绝对坐标
    Entryl = Entry(root,width=20)
    Entryl.place(x=110,y=1)
    Label(root,text='翻译的结果：',width=18).place(x=1,y=20)
    s = StringVar()
    s.set("大家好，这是测试")
    Entry2 = Entry(root,width=20)
    Entry2.place(x=110,y=20)
    Button1 = Button(root,text='翻译',width=8)
    Button1.place(x=40,y=80)
    Button2 = Button(root,text='清空',width=8)
    Button2.place(x=110,y=80)
    #给Button绑定鼠标监听事件
    Button1.bind("<Button-1>",leftClick)
    Button2.bind("<Button-1>",leftClick2)
    root.mainloop()