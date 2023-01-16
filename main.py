from tkinter import *
from tkcalendar import Calendar,DateEntry
from PIL import ImageTk,Image
from datetime import date
import sql_thngs,check_cred


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
    def clicked_signup():
        frame.grid_forget()
        sign_up()
    Label(image=my_img,bg="#90cad1").grid(row=0,column=0,rowspan=19,ipady=400)# Py Bank Logo

    Label(image=my_img3,bg="#90cad1").grid(row=0,column=1,pady=(300,0))# Py Bank Text Image
    #Label(win,text="Py Bank",font=20,bg="#90cad1",fg="black").grid(row=0,column=2,pady=60)

    frame=LabelFrame(win,bg="#90cad1",border=10,padx=100,pady=100)
    frame.grid(row=1,column=1)

    Label(frame,text="Username",bg="#90cad1",fg="black",font=15).grid(row=1,column=1,pady=30,padx=30)
    _username=Entry(frame,bg="white",fg='black')
    _username.grid(row=1,column=2,padx=(0,80))
    

    Label(frame,text="Password",bg="#90cad1",fg="black",font=15).grid(row=2,column=1)
    _password=Entry(frame,show='*',bg="white",fg='black').grid(row=2,column=2,padx=(0,80))
    
    Button(frame,text='Log In').grid(row=3,column=2,padx=(0,80),pady=30)
    Label(frame,text='OR',bg="#90cad1",fg="black").grid(row=4,column=2,padx=(0,80))
    Button(frame,text="Sign Up",command=clicked_signup).grid(row=5,column=2,pady=30,padx=(0,80))

    

def sign_up():
    """
        sign up page
    """
    frame2=LabelFrame(win,bg="#90cad1",border=10,padx=10,pady=10)

    gvals=[
        ("Male",'Male'),
        ("Female",'Female'),
        ("Other",'Other')
    ]
    gvar=StringVar(frame2,'male')
    frame2.grid(row=1,column=1)

    #Label(frame2,image=my_img2,bg="#90cad1").grid(row=0,column=1,pady=(45,0))

    Label(frame2,text="Sign up",font=100,bg='#90cad1',fg="black").grid(row=1,column=1,pady=(20,60),sticky="W")

    Label(frame2,text='            First name',bg="#90cad1",fg="black").grid(row=2,column=0)
    _fname=Entry(frame2,bg="white",fg='black').grid(row=2,column=1,padx=(0,100))

    Label(frame2,text='        Middle name',bg="#90cad1",fg="black").grid(row=3,column=0)
    _mname=Entry(frame2,bg="white",fg='black').grid(row=3,column=1,pady=30,padx=(0,100))

    Label(frame2,text='            Last name',bg="#90cad1",fg="black").grid(row=4,column=0)
    _lname=Entry(frame2,bg="white",fg='black').grid(row=4,column=1,padx=(0,100))

    Label(frame2,text='            Email Id',bg="#90cad1",fg="black").grid(row=5,column=0)
    _email=Entry(frame2,bg="white",fg='black').grid(row=5,column=1,pady=30,padx=(0,100))

    

    Label(frame2,text='      Date of Birth',bg="#90cad1",fg="black").grid(row=6,column=0)
    _dob=DateEntry(frame2,bg="white",fg='black')
    _dob.grid(row=6,column=1,ipadx=40,sticky="W")
    #_dob.insert(0,date.today())

    Label(frame2,text='Gender     ',bg='#90cad1',fg='black').grid(row=7,column=0,pady=(30,0),sticky='E')
    _rowcnt=7
    for text,mode in gvals:
        Radiobutton(frame2,fg='black',bg='#90cad1',text=text,variable=gvar, value=mode).grid(row=_rowcnt,column=1,sticky='WS',pady=5)
        _rowcnt+=1

    Label(frame2,text='            Password',bg="#90cad1",fg="black").grid(row=12,column=0,pady=(40,0))
    _passwrd=Entry(frame2,show='*',bg="white",fg='black').grid(row=12,column=1,padx=(0,100),pady=(40,0))

    Label(frame2,text='Confirm Password',bg="#90cad1",fg="black").grid(row=13,column=0,padx=(20,10))
    _cpasswrd=Entry(frame2,show='*',bg="white",fg='black').grid(row=13,column=1,pady=30,padx=(0,100))

    Button(frame2,text='Submit',bg="white",fg="black").grid(row=15,column=1,pady=30,padx=(0,100))



login_page()

win.mainloop()