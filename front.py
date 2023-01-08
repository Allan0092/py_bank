from tkinter import *
from PIL import ImageTk,Image
from datetime import date
import sql_thngs,regex


win = Tk()
win.title("Online Banking".center(100))
win.minsize(700,700)
win.maxsize(700,700)
win.config(background="white")

def login_page():
    """
        First login page
    """
    Label(win,text="Py Bank",font=10,bg="white",fg="black").grid(row=0,column=1,pady=60)

    Label(win,text="Username",bg="white",fg="black").grid(row=1,column=0,padx=(40,20))
    _login=Entry(win,bg="white",fg='black').grid(row=1,column=1)

    Label(win,text="  Password",bg="white",fg="black").grid(row=2,column=0)
    _password=Entry(win,show='*',bg="white",fg='black').grid(row=2,column=1,pady=30)
    
    Button(win,text='Login').grid(row=3,column=1,pady=(20,5))
    Label(win,text='or',bg="white",fg="black").grid(row=4,column=1,pady=10)
    Button(win,text="sign up",command=sign_up).grid(row=10,column=1)

def sign_up():
    """
        sign up page
    """
    win2=Toplevel(win)
    win2.minsize(900,1100)
    win2.maxsize(900,1100)
    win2.title("Online Banking Signup")

    win2.config(background='white')

    gvals=[
        ("Male",'Male'),
        ("Female",'Female'),
        ("Other",'Other')
    ]
    gvar=StringVar(win2,'male')

    Label(win2,text="Sign up",font=100,bg='white',fg="black").grid(row=0,column=1,pady=60)

    Label(win2,text='            First name',bg="white",fg="black").grid(row=1,column=0)
    _fname=Entry(win2,bg="white",fg='black').grid(row=1,column=1)

    Label(win2,text='        Middle name',bg="white",fg="black").grid(row=2,column=0)
    _mname=Entry(win2,bg="white",fg='black').grid(row=2,column=1,pady=30)

    Label(win2,text='            Last name',bg="white",fg="black").grid(row=3,column=0)
    _lname=Entry(win2,bg="white",fg='black').grid(row=3,column=1)

    Label(win2,text='            Email Id',bg="white",fg="black").grid(row=4,column=0)
    _email=Entry(win2,bg="white",fg='black').grid(row=4,column=1,pady=30)

    Label(win2,text='      Date of Birth',bg="white",fg="black").grid(row=5,column=0)
    _dob=Entry(win2,bg="white",fg='black')
    _dob.grid(row=5,column=1)
    _dob.insert(0,date.today())

    Label(win2,text='Gender',bg='white',fg='black').grid(row=6,column=0,pady=(30,0))
    for text,mode in gvals:
        Radiobutton(win2,fg='black',bg='white',text=text,variable=gvar, value=mode).grid(column=1,pady=5)

    Label(win2,text='            Password',bg="white",fg="black").grid(row=12,column=0,pady=(40,0))
    _passwrd=Entry(win2,show='*',bg="white",fg='black').grid(row=12,column=1)

    Label(win2,text='Confirm Password',bg="white",fg="black").grid(row=13,column=0,padx=(20,10))
    _cpasswrd=Entry(win2,show='*',bg="white",fg='black').grid(row=13,column=1,pady=30)

    Button(win2,text='Submit',bg="white",fg="black").grid(row=15,column=1,pady=30)

    
def check_credentials():
    pass

login_page()

win.mainloop()