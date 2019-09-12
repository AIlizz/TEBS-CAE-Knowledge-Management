#coding = utf-8
from tkinter import *
from tkinter import messagebox
import pandas as pd
import numpy as np

#关于布局的pack解析
#https://blog.csdn.net/superfanstoprogram/article/details/83713196


class Members:
    def __init__(self):
        # 读取members
        cols = ['user', 'code']
        self.path = '../00_Source/member_dist.txt'
        self.members = pd.read_csv(self.path, sep=' ', header=None, names=cols)

    def query(self):
        print(self.members)

    def login(self,userid_value,code_value):
        if userid_value in self.members['user'].values and \
                code_value == self.members.loc[self.members['user'] == userid_value]['code'].values[0]:
            if userid_value == 'admin':
                return 'admin'
            else:
                return 'success'
        elif userid_value in self.members['user'].values and \
                code_value != self.members.loc[self.members['user'] != userid_value]['code'].values[0]:
            return 'code_error'
        elif userid_value not in self.members['user'].values:
            return 'user_error'

    def add_member(self,userid_value,code1_value,code2_value):
        if userid_value in self.members['user'].values:
            return 'user_error'
        elif code1_value != code2_value:
            return 'code_error'
        else:
            i = self.members.shape[0]
            self.members.loc[i + 1] = [userid_value,code1_value]
            self.members.to_csv(self.path,sep = ' ',index = False,header= False)
            return 'success'

    def delete_member(self,userid_value,code_value):
        if userid_value in self.members['user'].values and \
                code_value == self.members.loc[self.members['user'] == userid_value]['code'].values[0]:
            self.members.drop(userid_value,axis = 0)
            return True
        else:
            return False

    def change_member(self,old_user,old_code,new_user,new_code1,new_code2):
        if self.delete_member(old_user,old_code):
            if self.add_member(new_user,new_code1,new_code2) == 'user_error':
                return 'new_user_exist'
            elif self.add_member(new_user,new_code1,new_code2) == 'code_error':
                return 'code_error'
            else:
                return 'success'
        else:
            return 'old_user_not_exist'

class Register:
    def __init__(self):
        root = Tk()
        root.title('新用户注册')

        # 定义账号密码的输入及登陆
        Label(root, text="请输入你的账号：", width=15).grid(row=0, column=1, sticky='W')
        Label(root, text="请输入你的密码：", width=15).grid(row=1, column=1, sticky='W')
        Label(root, text="请再次输入密码：", width=15).grid(row=2, column=1, sticky='W')
        self.userid = Entry(root, width=15)
        self.userid.grid(row=0, column=2, columnspan=2, sticky='E')
        self.code1 = Entry(root, width=15)
        self.code1['show'] = "*"  # 显示输入密码为*
        self.code1.grid(row=1, column=2, columnspan=2, sticky='E')
        self.code2 = Entry(root, width=15)
        self.code2['show'] = "*"  # 显示输入密码为*
        self.code2.grid(row=2, column=2, columnspan=2, sticky='E')

        Button(root, text="注册", relief=RAISED, command=self.reg, width=8).grid(row=4, column=1, columnspan=2)
        mainloop()

    def reg(self):
        try:
            userid_value = str(self.userid.get())
            code1_value = int(self.code1.get())
            code2_value = int(self.code2.get())
            state = Members().add_member(userid_value, code1_value, code2_value)
            if state == 'success':
                messagebox.showinfo(title='消息！', message='注册成功!')
            elif state == 'code_error':
                messagebox.showinfo(title='警告！', message='前后两个密码不相同!')
            elif state == 'user_error':
                messagebox.showinfo(title='警告！', message='该账号已经存在，请重新输入!')
        except:
            messagebox.showinfo(title='警告！', message='账户及密码不能为空!')


class Login:
    def __init__(self, name = 'CAE知识管理系统'):
        self.tk = Tk()
        #self.tk.geometry('180x100')
        self.tk.title(name)

        Label(self.tk, text="欢迎进入CAE知识管理系统", width=25).grid(row=0, column=0, columnspan=4)
        #定义账号密码的输入及登陆
        Label(self.tk, text="账号：", width=5).grid(row=1, column=1,sticky = 'W')
        Label(self.tk, text="密码：", width=5).grid(row=2, column=1,sticky = 'W')
        self.userid = Entry(self.tk, width=15)
        self.userid.grid(row=1, column=2, columnspan=2,sticky = 'E')
        self.code = Entry(self.tk, width=15)
        self.code['show'] = "*"# 显示输入密码为*
        self.code.grid(row=2, column=2, columnspan=2,sticky = 'E')

        Button(self.tk, text="忘记密码？", relief=FLAT, command=self.forget_code, width=8).grid(row=3, column=1)
        Button(self.tk, text="新用户注册", relief=FLAT, command=self.reg, width=8).grid(row=3, column=2)
        Button(self.tk, text="登陆", relief=RAISED, command=self.login, width=8).grid(row=4, column=1, columnspan=2)
        mainloop()

    def login(self):
        try:
            userid_value = str(self.userid.get())
            code_value = int(self.code.get())
            state = Members().login(userid_value,code_value)
            if state == 'success':
                self.tk.destroy()
                Work()#进入工作界面
            elif state == 'code_error':
                messagebox.showinfo(title='警告！', message='密码错误请重新输入!')
            elif state == 'user_error':
                messagebox.showinfo(title='警告！', message='该账号不存在请重新输入!')
        except:
            messagebox.showinfo(title='警告！', message='账户及密码不能为空!')

    def forget_code(self):
        messagebox.showinfo(title='忘记密码！', message='请联系管理员（Email:zhengzhu.li@faw-vw.com, Tel:82020276）!')

    def reg(self):
        Register()

class Work:
    def __init__(self,name = 'CAE知识管理系统'):
        self.tk = Tk()
        self.tk.geometry('900x600')
        self.tk.title(name)
        self.menu({'文件':['打开','导入','导出','保存','退出'],
        '编辑':['撤销','剪切','复制','粘贴','删除','全选'],
        '主数据':['用户管理','车辆种类','回收方法','材料种类','非实体零件规则','Mp/MD规则','拆解零件','质量验证'],
        '车型批准':['创建车型','编辑车型','复制车型','删除车型','导出清单'],
        '车型配置':['新建','复制','删除','对比','RRR(GB/T19515)','有害物质分析'],
        '窗口':['状态栏','工具栏','重置'],
        '帮助':['说明书','联系人']})
        Label(self.tk, text="车型列表区域", width=40).grid(row=0, column=0)
        Label(self.tk, text="零件列表(BOM)区域", width=40).grid(row=0, column=1)
        Label(self.tk, text="MDS展示区", width=40).grid(row=0, column=2)
        mainloop()

    def menu(self,menudict):
        mainmenu = Menu(self.tk)
        for firstmenu in menudict:
            secondmenu = Menu(mainmenu)
            for item in menudict[firstmenu]:
                secondmenu.add_command(label=item)
            mainmenu.add_cascade(label=firstmenu, menu=secondmenu)
        self.tk['menu'] = mainmenu

class Upload:
    def __init__(self):
        self.root = Tk()
        self.root.title('上传')

        fr1 = Frame(self.root)
        fr1.pack(side=TOP, fill=BOTH, expand=YES)
        fr2 = Frame(self.root)
        fr2.pack(side=TOP, fill=BOTH, expand=YES,pady=20)
        fr21 = Frame(fr2)
        fr21.pack(side=LEFT, fill=BOTH, expand=YES)
        fr22 = Frame(fr2)
        fr22.pack(side=LEFT, fill=BOTH, expand=YES)
        fr3 = Frame(self.root)
        fr3.pack(side=TOP, fill=BOTH, expand=YES)

        Label(fr1, text="你希望下载的文件：", width=15).pack(side = LEFT,fill =BOTH, expand = YES )
        self.file = Entry(fr1, width=30)
        self.file.pack(side = LEFT,fill =BOTH, expand = YES)
        Button(fr1, text="文件夹", relief=RAISED, command=self.pwd, width=8).pack(side=LEFT, fill=BOTH, expand=YES)

        Label(fr21, text="推荐你放在如下文件夹：", width=15).pack(side = TOP,fill =BOTH, expand = YES )
        self.path1 = Entry(fr21, width=30)
        self.path1.pack(side = TOP,fill =BOTH, expand = YES)
        Label(fr21, text="你还可以自定义路径：", width=15).pack(side=TOP, fill=BOTH, expand=YES)
        self.path2 = Entry(fr21, width=30)
        self.path2.pack(side=TOP, fill=BOTH, expand=YES)

        Label(fr22, text="推荐加上如下标签，方便后续搜索：", width=15).pack(side = TOP,fill =BOTH, expand = YES )
        self.label1 = Entry(fr22, width=30)
        self.label1.pack(side = TOP,fill =BOTH, expand = YES)
        Label(fr22, text="你还可以自定义标签：", width=15).pack(side=TOP, fill=BOTH, expand=YES)
        self.label2 = Entry(fr22, width=30)
        self.label2.pack(side=TOP, fill=BOTH, expand=YES)

        Button(fr3, text="取消", relief=RAISED, command=self.cancle, width=8).pack(side=RIGHT, fill=BOTH)
        Button(fr3, text="确认", relief=RAISED, command=self.download, width=8).pack(side = RIGHT, fill = BOTH)

        mainloop()

    def pwd(self):
        pass

    def download(self):
        pass

    def cancle(self):
        self.root.destroy()

class Download:
    def __init__(self):
        self.root = Tk()
        self.root.title('下载')

        fr1 = Frame(self.root)
        fr1.pack(side=TOP, fill=BOTH, expand=YES, pady=2)
        fr2 = Frame(self.root)
        fr2.pack(side=TOP, fill=BOTH, expand=YES, pady=2)
        fr3 = Frame(self.root)
        fr3.pack(side=TOP, fill=BOTH, expand=YES, pady=2)


        Label(fr1, text="你希望下载的文件：", width=15).pack(side=LEFT, fill=BOTH, expand=YES)
        self.file = Entry(fr1, width=39)
        self.file.pack(side=LEFT, fill=X, expand=YES)

        Label(fr2, text="将文件保存的位置：", width=15).pack(side=LEFT, fill=BOTH, expand=YES)
        self.path = Entry(fr2, width=30)
        self.path.pack(side=LEFT, fill=X, expand=YES)
        Button(fr2, text="文件夹", relief=RAISED, command=self.pwd, width=8).pack(side=LEFT, fill=BOTH, expand=YES)

        Button(fr3, text="确认", relief=RAISED, command=self.download, width=8).pack(side=LEFT, fill=NONE, expand=YES,anchor=E)
        Button(fr3, text="取消", relief=RAISED, command=self.cancle, width=8).pack(side=LEFT, fill=NONE, expand=YES,anchor=W)
        mainloop()

    def pwd(self):
        pass

    def download(self):
        pass

    def cancle(self):
        self.root.destroy()

if __name__ == '__main__':
    #Login()
    # M = Members()
    # M.add_member('admin',12345)
    # M.query()
    Download()
    #Upload()