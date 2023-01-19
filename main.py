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

IMAGE="images/logo"
IMAGE2="images/logo2"
IMAGE3="images/logo3.png"
IMAGE4="images/logo4c.png"
IMAGE5="images/logo5.png"
IMAGE6="images/logo6.png"

TITLE="images/title.png"

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

    global new_fname,new_lname,new_mname,new_email,new_dob,new_passwrd,new_cpasswrd,gvar

    frame2=LabelFrame(win,bg="#90cad1",border=10,padx=10,pady=10)

    gvals=[
        ("Male",'male'),
        ("Female",'female'),
        ("Other",'other')
    ]
    gvar=StringVar(frame2,'None')
    frame2.grid(row=1,column=1)

    #Label(frame2,image=my_img2,bg="#90cad1").grid(row=0,column=1,pady=(45,0))

    Label(frame2,text="Sign up",font=100,bg='#90cad1',fg="black").grid(row=1,column=1,pady=(20,60),sticky="W")

    Label(frame2,text='            First name',bg="#90cad1",fg="black").grid(row=2,column=0)
    new_fname=Entry(frame2,bg="white",fg='black')
    new_fname.grid(row=2,column=1,padx=(0,100))

    Label(frame2,text='        Middle name',bg="#90cad1",fg="black").grid(row=3,column=0)
    new_mname=Entry(frame2,bg="white",fg='black')
    new_mname.grid(row=3,column=1,pady=30,padx=(0,100))

    Label(frame2,text='            Last name',bg="#90cad1",fg="black").grid(row=4,column=0)
    new_lname=Entry(frame2,bg="white",fg='black')
    new_lname.grid(row=4,column=1,padx=(0,100))

    Label(frame2,text='            Email Id',bg="#90cad1",fg="black").grid(row=5,column=0)
    new_email=Entry(frame2,bg="white",fg='black')
    new_email.grid(row=5,column=1,pady=30,padx=(0,100))

    

    Label(frame2,text='      Date of Birth',bg="#90cad1",fg="black").grid(row=6,column=0)
    new_dob=DateEntry(frame2,bg="white",fg='black')
    new_dob.grid(row=6,column=1,ipadx=40,sticky="W")

    Label(frame2,text='Gender     ',bg='#90cad1',fg='black').grid(row=7,column=0,pady=(30,0),sticky='E')
    _rowcnt=7
    for text,mode in gvals:
        Radiobutton(frame2,fg='black',bg='#90cad1',text=text,variable=gvar, value=mode).grid(row=_rowcnt,column=1,sticky='WS',pady=5)
        _rowcnt+=1

    Label(frame2,text='            Password',bg="#90cad1",fg="black").grid(row=12,column=0,pady=(40,0))
    new_passwrd=Entry(frame2,show='*',bg="white",fg='black')
    new_passwrd.grid(row=12,column=1,padx=(0,100),pady=(40,0))

    Label(frame2,text='Confirm Password',bg="#90cad1",fg="black").grid(row=13,column=0,padx=(20,10))
    new_cpasswrd=Entry(frame2,show='*',bg="white",fg='black')
    new_cpasswrd.grid(row=13,column=1,pady=30,padx=(0,100))
    
    Button(frame2,text='Submit',bg="white",fg="black",command=sign_up_data).grid(row=15,column=1,pady=30,padx=(0,100))

def sign_up_data():
    print(f'First name {new_fname.get()}')
    print(f'Middle name {new_mname.get()}')
    print(f'Last name {new_lname.get()}')
    print(f'Email id {new_email.get()}')
    print(f'Date of Birth {new_dob.get_date()}')
    print(f'Gender {gvar.get()}')
    print(f'Password {new_passwrd.get()}')
    print(f'Confirm Password {new_cpasswrd.get()}')



login_page()

win.mainloop()