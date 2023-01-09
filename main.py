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
IMAGE4="py_bank/images/logo4c.png"
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
    Label(image=my_img,bg="#90cad1").grid(row=0,column=0,rowspan=19,ipady=400)# Py Bank Logo

    Label(image=my_img3,bg="#90cad1").grid(row=0,column=1,pady=(300,0))# Py Bank Text Image
    #Label(win,text="Py Bank",font=20,bg="#90cad1",fg="black").grid(row=0,column=2,pady=60)

    frame=LabelFrame(win,bg="#90cad1",border=10,padx=100,pady=100)
    frame.grid(row=1,column=1)

    Label(frame,text="Username",bg="#90cad1",fg="black",font=15).grid(row=1,column=1,pady=30,padx=30)
    _username=Entry(frame,bg="white",fg='black').grid(row=1,column=2,padx=(0,80))

    Label(frame,text="Password",bg="#90cad1",fg="black",font=15).grid(row=2,column=1)
    _password=Entry(frame,show='*',bg="white",fg='black').grid(row=2,column=2,padx=(0,80))
    
    Button(frame,text='Log In').grid(row=3,column=2,padx=(0,80),pady=30)
    Label(frame,text='OR',bg="#90cad1",fg="black").grid(row=4,column=2,padx=(0,80))
    Button(frame,text="Sign Up",command=sign_up).grid(row=5,column=2,pady=30,padx=(0,80))

def sign_up():
    """
        sign up page
    """
    win2=Toplevel(win)
    win2.minsize(900,1200)
    win2.maxsize(900,1500)
    win2.title("Online Banking Signup")

    win2.config(background='#90cad1')

    gvals=[
        ("Male",'Male'),
        ("Female",'Female'),
        ("Other",'Other')
    ]
    gvar=StringVar(win2,'male')

    Label(win2,image=my_img2,bg="#90cad1").grid(row=0,column=1,pady=(45,0))

    Label(win2,text="Sign up",font=100,bg='#90cad1',fg="black").grid(row=1,column=1,pady=(20,60))

    Label(win2,text='            First name',bg="#90cad1",fg="black").grid(row=2,column=0)
    _fname=Entry(win2,bg="white",fg='black').grid(row=2,column=1)

    Label(win2,text='        Middle name',bg="#90cad1",fg="black").grid(row=3,column=0)
    _mname=Entry(win2,bg="white",fg='black').grid(row=3,column=1,pady=30)

    Label(win2,text='            Last name',bg="#90cad1",fg="black").grid(row=4,column=0)
    _lname=Entry(win2,bg="white",fg='black').grid(row=4,column=1)

    Label(win2,text='            Email Id',bg="#90cad1",fg="black").grid(row=5,column=0)
    _email=Entry(win2,bg="white",fg='black').grid(row=5,column=1,pady=30)

    Label(win2,text='      Date of Birth',bg="#90cad1",fg="black").grid(row=6,column=0)
    _dob=Entry(win2,bg="white",fg='black')
    _dob.grid(row=6,column=1)
    _dob.insert(0,date.today())

    Label(win2,text='Gender     ',bg='#90cad1',fg='black').grid(row=7,column=0,pady=(30,0),sticky='E')
    _rowcnt=7
    for text,mode in gvals:
        Radiobutton(win2,fg='black',bg='#90cad1',text=text,variable=gvar, value=mode).grid(row=_rowcnt,column=1,sticky='WS',pady=5)
        _rowcnt+=1

    Label(win2,text='            Password',bg="#90cad1",fg="black").grid(row=12,column=0,pady=(40,0))
    _passwrd=Entry(win2,show='*',bg="white",fg='black').grid(row=12,column=1)

    Label(win2,text='Confirm Password',bg="#90cad1",fg="black").grid(row=13,column=0,padx=(20,10))
    _cpasswrd=Entry(win2,show='*',bg="white",fg='black').grid(row=13,column=1,pady=30)

    Button(win2,text='Submit',bg="white",fg="black").grid(row=15,column=1,pady=30)


login_page()

win.mainloop()