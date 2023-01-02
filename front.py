from tkinter import *
from PIL import ImageTk,Image
import sql_thngs


win = Tk()
win.title("Online Banking".center(100))
win.minsize(700,700)
win.maxsize(700,700)
win.config(background="white")

def login_page():
    Label(win,text="Py Bank",font=10,bg="white",fg="black").place(x=300,y=50)

    Label(win,text="username",bg="white",fg="black").place(x=80,y=200)
    _login=Entry(win,bg="white",fg='black').place(x=230,y=200)
    Label(win,text="password",bg="white",fg="black").place(x=80,y=250)
    _password=Entry(win,show='*',bg="white",fg='black').place(x=230,y=250)
    Button(win,text='login').place(x=320,y=330)
    Label(win,text='or',bg="white",fg="black").place(x=350,y=400)
    Button(win,text="sign up",command=sign_up).place(x=305,y=450)

def sign_up():
    win2=Toplevel(win)
    win2.minsize(900,900)
    win2.maxsize(900,900)

    win2.config(background='white')

    Label(win2,text="Sign up",font=100,bg='white',fg="black").place(x=400,y=80)

    Label(win2,text='first name',bg="white",fg="black").place(x=150,y=200)
    _fname=Entry(win2,bg="white",fg='black').place(x=300,y=200)
    Label(win2,text='middle name',bg="white",fg="black").place(x=115,y=280)
    _mname=Entry(win2,bg="white",fg='black').place(x=300,y=280)
    Label(win2,text='last name',bg="white",fg="black").place(x=155,y=360)
    _lname=Entry(win2,bg="white",fg='black').place(x=300,y=360)
    Label(win2,text='email id',bg="white",fg="black").place(x=175,y=440)
    _email=Entry(win2,bg="white",fg='black').place(x=300,y=440)
    Label(win2,text='password',bg="white",fg="black").place(x=155,y=520)
    _passwrd=Entry(win2,show='*',bg="white",fg='black').place(x=300,y=520)
    Label(win2,text='confirm password',bg="white",fg="black").place(x=50,y=600)
    _cpasswrd=Entry(win2,show='*',bg="white",fg='black').place(x=300,y=600)
    
    Button(win2,text='submit',bg="white",fg="black").place(x=400,y=700)

def check_credentials():
    pass

login_page()

win.mainloop()