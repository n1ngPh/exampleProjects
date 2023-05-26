# -*- coding:utf-8 -*-
# @Time : 2022/4/25 12:22
# @File : gui.py
# @Software : PyCharm

from tkinter import *
import dbData



class GUI():

    def __init__(self):
        pass

    def main(self):
        self.root = Tk()
        # 对应的格式为宽乘以高加上水平偏移量加上垂直偏移量
        self.root.geometry("400x400+200+200")
        label = Label(self.root, text="电影查询系统", font=("华文行楷", 20))
        # 调用pack方法将label标签显示在主界面
        label.pack()
        rootbutton = Button(self.root, text='初始化(加载数据)', command=self.callbackroot, width=20)
        rootbutton.pack()

        mainbutton = Button(self.root, text='开始运行', command=self.callbackmain, width=20, height=3)
        mainbutton.pack()
        self.root.mainloop()

    def callbackroot(self):

        dbData.main()
        print("数据加载完成！可以点击开始运行了")


    def callbackmain(self):
        # 关闭窗口
        self.root.destroy()
        # 启动电影查询系统
        import app
        app.main()

GUI().main()
