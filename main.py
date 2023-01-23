from tkinter import *
from tkcalendar import DateEntry
from PIL import ImageTk,Image
import sql_thngs,check_cred


win = Tk()
win.title("Online Banking".center(100))
win.minsize(2560,1600)
#win.maxsize(1500,800)
BACKGROUND1="#90cad1"
BACKGROUND2="white"
FOREGROUND1='black'
win.config(background=BACKGROUND1)

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
    py_bank_logo=Label(image=my_img,bg=BACKGROUND1)
    py_bank_logo.grid(row=0,column=0,rowspan=19,ipady=400)# Py Bank Logo

    py_bank_title=Label(image=my_img3,bg=BACKGROUND1)
    py_bank_title.grid(row=0,column=1,pady=(300,0))# Py Bank Text Image
    #Label(win,text="Py Bank",font=20,bg=BACKGROUND1,fg=FOREGROUND1).grid(row=0,column=2,pady=60)

    frame=LabelFrame(win,bg=BACKGROUND1,border=10,padx=100,pady=100)
    frame.grid(row=1,column=1)

    Label(frame,text="Username",bg=BACKGROUND1,fg=FOREGROUND1,font=15).grid(row=1,column=1,pady=30,padx=30)
    _username=Entry(frame,bg=BACKGROUND2,fg=FOREGROUND1)
    _username.grid(row=1,column=2,padx=(0,80))
    

    Label(frame,text="Password",bg=BACKGROUND1,fg=FOREGROUND1,font=15).grid(row=2,column=1)
    _password=Entry(frame,show='*',bg=BACKGROUND2,fg=FOREGROUND1).grid(row=2,column=2,padx=(0,80))
    
    Button(frame,text='Log In').grid(row=3,column=2,padx=(0,80),pady=30)
    Label(frame,text='OR',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=4,column=2,padx=(0,80))
    Button(frame,text="Sign Up",command=clicked_signup).grid(row=5,column=2,pady=30,padx=(0,80))

    

def sign_up():
    """
        sign up page
    """

    global frame2,new_fname,new_lname,new_mname,new_email,new_dob,new_passwrd,new_cpasswrd,gvar,new_uname

    frame2=LabelFrame(win,bg=BACKGROUND1,border=10,padx=10,pady=10)

    gvals=[
        ("Male",'male'),
        ("Female",'female'),
        ("Other",'other')
    ]
    gvar=StringVar(frame2,'None')
    frame2.grid(row=1,column=1)

    #Label(frame2,image=my_img2,bg=BACKGROUND1).grid(row=0,column=1,pady=(45,0))

    Label(frame2,text="Sign up",font=100,bg='#90cad1',fg=FOREGROUND1).grid(row=1,column=1,pady=(20,60),sticky="W")

    Label(frame2,text='            First name',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=2,column=0)
    new_fname=Entry(frame2,bg=BACKGROUND2,fg=FOREGROUND1)
    new_fname.grid(row=2,column=1,padx=(0,100))

    Label(frame2,text='        Middle name',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=4,column=0)
    new_mname=Entry(frame2,bg=BACKGROUND2,fg=FOREGROUND1)
    new_mname.grid(row=4,column=1,pady=30,padx=(0,100))

    Label(frame2,text='            Last name',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=6,column=0)
    new_lname=Entry(frame2,bg=BACKGROUND2,fg=FOREGROUND1)
    new_lname.grid(row=6,column=1,padx=(0,100))

    Label(frame2,text='            Email Id',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=8,column=0)
    new_email=Entry(frame2,bg=BACKGROUND2,fg=FOREGROUND1)
    new_email.grid(row=8,column=1,pady=(30,0),padx=(0,100))

    Label(frame2,text='      Date of Birth',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=10,column=0)
    new_dob=DateEntry(frame2,bg=BACKGROUND2,fg=FOREGROUND1)
    new_dob.grid(row=10,column=1,ipadx=40,sticky="W",pady=(30,0))

    Label(frame2,text='Gender     ',bg='#90cad1',fg=FOREGROUND1).grid(row=12,column=0,pady=(30,0),sticky='E')
    _rowcnt=12
    for text,mode in gvals:
        Radiobutton(frame2,fg=FOREGROUND1,bg='#90cad1',text=text,variable=gvar, value=mode).grid(row=_rowcnt,column=1,sticky='WS',pady=5)
        _rowcnt+=1

    Label(frame2,text="             Username",bg=BACKGROUND1,fg=FOREGROUND1).grid(row=16,column=0,pady=(40,0))
    new_uname=Entry(frame2,bg=BACKGROUND2,fg=FOREGROUND1)
    new_uname.grid(row=16,column=1,sticky='W',pady=(40,0))

    Label(frame2,text='            Password',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=18,column=0,pady=(40,0))
    new_passwrd=Entry(frame2,show='*',bg=BACKGROUND2,fg=FOREGROUND1)
    new_passwrd.grid(row=18,column=1,padx=(0,100),pady=(40,0))

    Label(frame2,text='Confirm Password',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=20,column=0,padx=(20,10))
    new_cpasswrd=Entry(frame2,show='*',bg=BACKGROUND2,fg=FOREGROUND1)
    new_cpasswrd.grid(row=20,column=1,pady=(30,0),padx=(0,100))
    
    Button(frame2,text='Submit',bg=BACKGROUND2,fg=FOREGROUND1,command=sign_up_data).grid(row=22,column=1,pady=60,padx=(0,100))

def sign_up_data():
    global all_data

    print(f'First name {new_fname.get()}')
    print(f'Middle name {new_mname.get()}')
    print(f'Last name {new_lname.get()}')
    print(f'Email id {new_email.get()}')
    print(f'Date of Birth {new_dob.get_date()}')
    print(f'Gender {gvar.get()}')
    print(f'Username {new_uname.get()}')
    print(f'Password {new_passwrd.get()}')
    print(f'Confirm Password {new_cpasswrd.get()}')
    print()

    data_fname=new_fname.get()
    data_fname=data_fname.strip()
    data_mname=new_mname.get()
    data_lname=new_lname.get()
    data_email=new_email.get()
    data_dob=new_dob.get_date()
    data_dob=str(data_dob)
    data_uname=new_uname.get()
    data_passwrd=new_passwrd.get()
    data_confpasswrd=new_cpasswrd.get()
    data_gender=gvar.get()

    all_data=[data_fname, data_mname, data_lname, data_email, data_dob, data_uname, data_passwrd, data_confpasswrd,data_gender]

    _check_data=check_cred.main(all_data)
    print(f'check : {_check_data}')
    if not _check_data[0]:
        signup_error_show(_check_data)

    
def signup_error_show(_where):
    global signup_error1

    #[symbol number, field name, row]
    error_codes=[
        [0, 'first name', 3],
        [1 , 'middle name', 5],
        [2 , 'last name', 7],
        [3 , 'email', 9],
        [4 , 'date of birth', 11],
        [5 , 'username', 17],
        [6 , 'password', 19],
        [7 , 'confirm password', 21],
        [8 , 'gender', 15]
    ]

    try:
        signup_error1.grid_forget()
    except NameError:
        pass

    _row=error_codes[_where[1]][2]
    _text=error_codes[_where[1]][1]
    print(f'\nError : {_text}\nat {_row}')

    signup_error1=Label(frame2,text=_text + _where[2],fg='red')
    signup_error1.grid(row=_row,column=1,columnspan=4,sticky='WN')

    


login_page()

win.mainloop()