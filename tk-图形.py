from tkinter import *
root=Tk()


button1=Button(root,text="确定")
button1.config(text="确定")
button1 ["text"]="确定"
root.title("我的窗口")
labl=Label(root,text='你好',anchor='nw')
labl.pack()
lab2=Label(root,bitmap='question')
lab2.pack()

bm=PhotoImage(file=r'F:\图片\QQ图片20190322123319.png')#请更改正确的地址
lab3=Label(root,image=bm)
lab3.bm=bm
lab3.pack()
root.mainloop()
