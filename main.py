# coding:utf-8
"""
Author: Edgar
"""
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import json


# 创建主窗口
window = Tk()
window.title("Welcome")
window.geometry("500x400")
window.resizable(width=False, height=False)
# 首页的图片
image = Image.open("./welcome.jpg")
img = ImageTk.PhotoImage(image, size=10)
c = Canvas(window, width=500, height=200)
c.create_image(250, 0, image=img, anchor=N)

# 提前打开并保存该图片对象，如果之后再函数中定义打开可能会报错
img_2 = Image.open("./sign_up.jpg")
img_2 = ImageTk.PhotoImage(img_2)
# 打包好，使其能够显示在屏幕上
c.pack()

# 显示信息
# messagebox.showinfo(title='Status', message='图片下载完成！开始生成图片') # 添加该信息之后可能刚开始不能点击输入框

# 提示文字，账号和密码
username_label = Label(window, font='Monaco 12', text="username:")
passwd_label = Label(window, font='Monaco 12', text='password:')

# 摆放相关的位置
username_label.place(x=40, y=220)
passwd_label.place(x=40, y=260)

welcome = Label(window, font="monaco 12", text='Welcome here to learn python !')
welcome.place(x=250, y=320, anchor=N)
# 输入框
username = StringVar()
passwd = StringVar()
username_entry = Entry(window, font='Monaco 10', width=20, textvariable=username)
passwd_entry = Entry(window, font='Monaco 10', width=20, textvariable=passwd, show='*')

username_entry.place(x=150, y=225)
passwd_entry.place(x=150, y=265)


# 提交登录
def login():
    user = username.get()
    password = passwd.get()
    # 获取用户输入的账号密码
    if str(user) and str(password):
        # 如果两个输入框都填写了，才进行相关操作
        try:
            # 打开数据保存文件，查找对应的信息
            with open('./data.json', 'r') as file:
                data = json.load(file)
                if user in data:
                    if password == data[user]:
                        messagebox.showinfo(title='Successfully', message="Login in susscessfully")
                        """
                        登录成功后可以在这里进行操作
                        """
                    else:
                        # 账号存在，密码错误，提示
                        messagebox.showerror(title='Error', message='password is wrong')
                else:
                    # 无账号，提示是否进行注册
                    flag = messagebox.askyesno(title='sign up',
                                               message='You have not signed up, do you want to sign up')
                    if flag:
                        # 进行注册
                        sign_up()
                    else:
                        # 不注册关闭根窗口
                        window.destroy()
        except:
            with open('./data.json', 'w') as file:
                admin = {"admin": "Cyberist"}
                json.dump(admin, file)
                if user == 'admin' and password == 'Cyberist':
                    messagebox.showinfo(title='Successfully', message="Login in susscessfully")
                else:
                    messagebox.showerror(title='Error', message='password is wrong')
    else:
        # 没有填写完输入框
        messagebox.showerror(title="Error", message='Fill in all the blank')


def sign_up():
    """
    数显注册的功能
    """

    def write_in():
        """
        将用户的信息写入数据文件中
        """
        if str(new_passwd.get()) and str(new_user.get()) and str(new_passwd_confirm.get()):
            # 输入框全部填写才能进行操作
            if new_passwd_confirm.get() == new_passwd.get():
                # 如果两次输入的密码一致
                try:
                    file = open("./data.json", "r")
                    data = json.load(file)
                    file.close()
                    if str(new_user.get()) in data:
                        # 账号已经在文件中
                        messagebox.showinfo(title='Error', message='The username has been signed')
                    else:
                        user = str(new_user.get())
                        passwd = new_passwd.get()
                        data[user] = passwd
                        with open('./data.json', 'w') as file:
                            json.dump(data, file)
                        messagebox.showinfo(message="Sign up finished", title='Successfully')
                        win.destroy()
                except Exception as e:
                    pass
            else:
                messagebox.showerror(title='Error', message='The confirmed password is not right !')
        else:
            messagebox.showerror(title='Error', message='Fill in all the blank !')

    win = Toplevel()
    # win.resizable(width=False, height=False)
    win.title("Sign up")
    win.geometry('400x300')
    win.wm_attributes('-topmost', -1)

    # 添加图片
    win_c = Canvas(win)
    win_c.create_image(190, 150, image=img_2)
    # win.attributes('-alpha', 0.3)  # 可以设置透明度
    win_c.pack()

    prompt = Label(win, text='Cyberist -- a python learner', font='Monaco 8')
    prompt.place(x=100, y=270)

    # 相关的账号，密码，核对密码文字
    user_label = Label(win, text='username:', font='monaco 10', bg=None)
    pwd_label = Label(win, text='password:', font='monaco 10')
    pwd_confirm_label = Label(win, text='confirm:', font='monaco 10')

    # 摆放位置
    user_label.place(x=20, y=180)
    pwd_label.place(x=20, y=210)
    pwd_confirm_label.place(x=20, y=240)

    # 定义相关的变量，获取用户的输入信息
    new_user = StringVar()
    new_passwd = StringVar()
    new_passwd_confirm = StringVar()

    # 相关的输入框
    user_entry = Entry(win, font='Monaco 12', width=20, textvariable=new_user)
    passwd_entry = Entry(win, font='Monaco 12', width=20, textvariable=new_passwd, show='*')
    passwd_confirm_entry = Entry(win, font='Monaco 12', width=20, textvariable=new_passwd_confirm, show='*')

    # 根据之前在登录界面的用户名填写
    tmp_username = username.get()
    new_user.set(tmp_username)

    user_entry.place(x=100, y=180)
    passwd_entry.place(x=100, y=210)
    passwd_confirm_entry.place(x=100, y=240)
    sign_up_button = Button(win, text='sign up', font='Monaco 10', command=write_in)
    sign_up_button.place(x=310, y=210)


# 登录的按钮
login_button = Button(window, width=8, text='Login in', font='Monaco 10', borderwidth=1, command=login)

# 注册的按钮
sign_up_buttom = Button(window, width=8, text='Sign up', font='Monaco 10', borderwidth=1, command=sign_up)

login_button.place(x=360, y=260)
sign_up_buttom.place(x=360, y=220)

# 调用mainloop方法，不断监听用户信息，并显示界面，否则只是一闪而过
window.mainloop()
