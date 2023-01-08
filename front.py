from tkinter import *
from PIL import ImageTk,Image
from datetime import date
import sql_thngs,regex


win = Tk()
win.title("Online Banking".center(100))
win.minsize(2560,1600)
#win.maxsize(1500,800)
win.config(background="#90cad1")

IMAGE="py_bank/images/logo"
IMAGE2="py_bank/images/logo2"
IMAGE3="py_bank/images/logo3.png"
IMAGE4="py_bank/images/logo4.png"
IMAGE5="py_bank/images/logo5.png"
IMAGE6="py_bank/images/logo6.png"

TITLE="py_bank/images/title.png"

my_img=ImageTk.PhotoImage(Image.open(IMAGE6))# login page
my_img2=ImageTk.PhotoImage(Image.open(IMAGE4),size=(1,1))# signup page
my_img3=ImageTk.PhotoImage(Image.open(TITLE),size=(1,1))# py_bank

def login_page():
    """
        First login page
    """
    Label(image=my_img,bg="#90cad1").grid(row=0,column=0,rowspan=19,ipady=400)

    Label(image=my_img3,bg="#90cad1").grid(row=0,column=2,pady=(500,0))# Py Bank Image
    #Label(win,text="Py Bank",font=20,bg="#90cad1",fg="black").grid(row=0,column=2,pady=60)

    Label(win,text="Username",bg="#90cad1",fg="black",font=15).grid(row=1,column=1,ipadx=20)
    _login=Entry(win,bg="white",fg='black').grid(row=1,column=2)

    Label(win,text="Password",bg="#90cad1",fg="black",font=15).grid(row=2,column=1)
    _password=Entry(win,show='*',bg="white",fg='black').grid(row=2,column=2)
    
    Button(win,text='Log In').grid(row=3,column=2)
    Label(win,text='OR',bg="#90cad1",fg="black").grid(row=4,column=2)
    Button(win,text="Sign Up",command=sign_up).grid(row=5,column=2)

def sign_up():
    """
        sign up page
    """
    win2=Toplevel(win)
    win2.minsize(900,1100)
    win2.maxsize(900,1500)
    win2.title("Online Banking Signup")

    win2.config(background='white')

    gvals=[
        ("Male",'Male'),
        ("Female",'Female'),
        ("Other",'Other')
    ]
    gvar=StringVar(win2,'male')

    Label(win2,image=my_img2).grid(row=0,column=1,pady=(45,0))

    Label(win2,text="Sign up",font=100,bg='white',fg="black").grid(row=1,column=1,pady=(20,60))

    Label(win2,text='            First name',bg="white",fg="black").grid(row=2,column=0)
    _fname=Entry(win2,bg="white",fg='black').grid(row=2,column=1)

    Label(win2,text='        Middle name',bg="white",fg="black").grid(row=3,column=0)
    _mname=Entry(win2,bg="white",fg='black').grid(row=3,column=1,pady=30)

    Label(win2,text='            Last name',bg="white",fg="black").grid(row=4,column=0)
    _lname=Entry(win2,bg="white",fg='black').grid(row=4,column=1)

    Label(win2,text='            Email Id',bg="white",fg="black").grid(row=5,column=0)
    _email=Entry(win2,bg="white",fg='black').grid(row=5,column=1,pady=30)

    Label(win2,text='      Date of Birth',bg="white",fg="black").grid(row=6,column=0)
    _dob=Entry(win2,bg="white",fg='black')
    _dob.grid(row=6,column=1)
    _dob.insert(0,date.today())

    Label(win2,text='Gender',bg='white',fg='black').grid(row=7,column=0,pady=(30,0))
    for text,mode in gvals:
        Radiobutton(win2,fg='black',bg='white',text=text,variable=gvar, value=mode).grid(column=1,pady=5)

    Label(win2,text='            Password',bg="white",fg="black").grid(row=12,column=0,pady=(40,0))
    _passwrd=Entry(win2,show='*',bg="white",fg='black').grid(row=12,column=1)

    Label(win2,text='Confirm Password',bg="white",fg="black").grid(row=13,column=0,padx=(20,10))
    _cpasswrd=Entry(win2,show='*',bg="white",fg='black').grid(row=13,column=1,pady=30)

    Button(win2,text='Submit',bg="white",fg="black").grid(row=15,column=1,pady=30)


login_page()

win.mainloop()