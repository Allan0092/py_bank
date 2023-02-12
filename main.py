from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import ImageTk,Image

import check_cred,DataActions


def login_page():
    """
        First login page
    """
    global login_frame,login_username,login_password,py_bank_logo,py_bank_title

    def clicked_signup():
        login_frame.grid_forget()
        py_bank_title.grid_forget()
        sign_up()

    py_bank_logo=Label(image=my_img,bg=BACKGROUND1)
    py_bank_logo.grid(row=0,column=0,rowspan=19,ipady=400)# Py Bank Logo

    py_bank_title=Label(image=my_img3,bg=BACKGROUND1)
    py_bank_title.grid(row=0,column=1,pady=(300,0))# Py Bank Text Image
    #Label(win,text="Py Bank",font=20,bg=BACKGROUND1,fg=FOREGROUND1).grid(row=0,column=2,pady=60)

    login_frame=LabelFrame(win,bg=BACKGROUND1,border=10,padx=100,pady=100)
    login_frame.grid(row=1,column=1)

    Label(login_frame,text="Username",bg=BACKGROUND1,fg=FOREGROUND1,font=15).grid(row=1,column=1,padx=30)
    login_username=Entry(login_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    login_username.grid(row=1,column=2,padx=(0,80))
    

    Label(login_frame,text="Password",bg=BACKGROUND1,fg=FOREGROUND1,font=15).grid(row=3,column=1,pady=(30,0))
    login_password=Entry(login_frame,show='*',bg=BACKGROUND2,fg=FOREGROUND1)
    login_password.grid(row=3,column=2,padx=(0,80),sticky="S")
    
    Button(login_frame,text='Log In',command=login_check).grid(row=5,column=2,padx=(0,80),pady=30)

    Label(login_frame,text='OR',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=6,column=2,padx=(0,80))
    Label(login_frame,text="Don't have an account?",bg=BACKGROUND1).grid(row=8,column=1,sticky='E')

    Button(login_frame,text="Sign Up",command=clicked_signup).grid(row=8,column=2,pady=30,padx=(0,80))

def login_check():
    """
        Checks username and password
    """
    global logged_in_name

    try:
        login_error1.grid_forget()
        login_error2.grid_forget()
    except NameError:
        pass

    all_clients=DataActions.retrieve_all()

    for client in all_clients:
        if login_username.get()==client[6]:
            if login_password.get()==client[7]:
                login_frame.grid_forget()
                py_bank_logo.grid_forget()
                py_bank_title.grid_forget()
                logged_in_name=f"{client[0]} {client[2]}"
                homepage()    
            else:
                login_error_show(2)# Wrong password
        else:
            login_error_show(1)# Username not found
    
def login_error_show(what:int):
    """
        shows username not found and password is incorrect errors.

            1 : Username not found
            2: Password is incorrect
    """
    global login_error1, login_error2

    login_error1=Label(login_frame,text="Username not found",fg='red',bg=BACKGROUND1)
    login_error2=Label(login_frame,text="Password is incorrect",fg="red",bg=BACKGROUND1)

    if what==1:
        login_error1.grid(row=2,column=2,sticky="WN")
    elif what==2:
        login_error2.grid(row=4, column=2,sticky="WN")

def sign_up():
    """
        sign up page
    """

    global signup_frame,new_fname,new_lname,new_mname,new_email,new_dob,new_passwrd,new_cpasswrd,gvar,new_uname

    py_bank_title.grid(row=0,column=1,pady=(200,0))
    signup_frame=LabelFrame(win,bg=BACKGROUND1,border=10,padx=10,pady=10)
    signup_frame.grid(row=1,column=1)

    def clicked_login():
        signup_frame.grid_forget()
        py_bank_title.grid_forget()
        py_bank_logo.grid_forget()
        login_page()

    gvals=[
        ("Male",'male'),
        ("Female",'female'),
        ("Other",'other')
    ]
    gvar=StringVar(signup_frame,'None')
    
    #Label(frame2,image=my_img2,bg=BACKGROUND1).grid(row=0,column=1,pady=(45,0))

    Label(signup_frame,text="Sign up",font=100,bg='#90cad1',fg=FOREGROUND1).grid(row=1,column=1,pady=(20,60),sticky="W")

    Label(signup_frame,text='            First name',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=2,column=0)
    new_fname=Entry(signup_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    new_fname.grid(row=2,column=1,padx=(0,100))

    Label(signup_frame,text='        Middle name',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=4,column=0)
    new_mname=Entry(signup_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    new_mname.grid(row=4,column=1,pady=30,padx=(0,100))

    Label(signup_frame,text='            Last name',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=6,column=0)
    new_lname=Entry(signup_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    new_lname.grid(row=6,column=1,padx=(0,100))

    Label(signup_frame,text='            Email Id',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=8,column=0,sticky="S")
    new_email=Entry(signup_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    new_email.grid(row=8,column=1,pady=(30,0),padx=(0,100))

    Label(signup_frame,text='      Date of Birth',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=10,column=0,sticky="S")
    new_dob=DateEntry(signup_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    new_dob.grid(row=10,column=1,ipadx=40,sticky="W",pady=(30,0))

    Label(signup_frame,text='Gender     ',bg='#90cad1',fg=FOREGROUND1).grid(row=12,column=0,pady=(30,0),sticky='E')
    _rowcnt=12
    for text,mode in gvals:
        Radiobutton(signup_frame,fg=FOREGROUND1,bg='#90cad1',text=text,variable=gvar, value=mode).grid(row=_rowcnt,column=1,sticky='WS',pady=5)
        _rowcnt+=1

    Label(signup_frame,text="             Username",bg=BACKGROUND1,fg=FOREGROUND1).grid(row=16,column=0,pady=(40,0))
    new_uname=Entry(signup_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    new_uname.grid(row=16,column=1,sticky='W',pady=(40,0))

    Label(signup_frame,text='            Password',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=18,column=0,pady=(40,0))
    new_passwrd=Entry(signup_frame,show='*',bg=BACKGROUND2,fg=FOREGROUND1)
    new_passwrd.grid(row=18,column=1,padx=(0,100),pady=(40,0))

    Label(signup_frame,text='Confirm Password',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=20,column=0,padx=(20,10),sticky='S')
    new_cpasswrd=Entry(signup_frame,show='*',bg=BACKGROUND2,fg=FOREGROUND1)
    new_cpasswrd.grid(row=20,column=1,pady=(30,0),padx=(0,100))
    
    Button(signup_frame,text='Submit',fg=FOREGROUND1,command=sign_up_data).grid(row=22,column=1,pady=(60,0),padx=(0,100))

    Label(signup_frame,text='OR',bg=BACKGROUND1).grid(row=23, column=1,padx=(0,100),pady=25)
    Button(signup_frame,text='Log in',fg=FOREGROUND1,command=clicked_login).grid(row=24,column=1,pady=(0,20),padx=(0,100))

def sign_up_data():
    global all_data

    # print(f'First name {new_fname.get()}')
    # print(f'Middle name {new_mname.get()}')
    # print(f'Last name {new_lname.get()}')
    # print(f'Email id {new_email.get()}')
    # print(f'Date of Birth {new_dob.get_date()}')
    # print(f'Gender {gvar.get()}')
    # print(f'Username {new_uname.get()}')
    # print(f'Password {new_passwrd.get()}')
    # print(f'Confirm Password {new_cpasswrd.get()}')
    # print()

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
    # print(f'check : {_check_data}')

    if not _check_data[0]:# Error found
        signup_error_show(_check_data)

    else:# Everything OK
        DataActions.signup_submit(all_data)
        messagebox.showinfo("Success","Submitted Sucessfully")
        
def signup_error_show(_where:list) -> None:
    """
        displays the error message at sign up page
    """

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
    # print(f'\nError : {_text}\nat {_row}')

    signup_error1=Label(signup_frame,text=_text + _where[2],fg='red',bg=BACKGROUND1)
    signup_error1.grid(row=_row,column=1,columnspan=4,sticky='WN')

def homepage():
    """
        The homepage, after login is successfull.
    """

    homepage_PybankLogo=Label(win,image=my_img7)
    homepage_PybankLogo.grid(row=0,column=0,rowspan=3)

    Label(win,text=f"Welcome {logged_in_name},").grid(row=0,column=1)

    homepage_frame1=LabelFrame(win)
    homepage_frame1.grid(row=1,column=1)
    Label(homepage_frame1,text="Account Number").grid(row=0,column=0)

    homepage_frame2=LabelFrame(win,borderwidth=5)
    homepage_frame2.grid(row=2,column=1,sticky="N")
    Label(homepage_frame2,text='XXXXXXXXXX').grid(row=0,column=0)

    homepage_frame3=LabelFrame(win)
    homepage_frame3.grid(row=1,column=2)
    Label(homepage_frame3,text="Account Balance").grid(row=0,column=0)

    homepage_frame4=LabelFrame(win)
    homepage_frame4.grid(row=2,column=2,sticky="N")
    Label(homepage_frame4,text='20,000').grid(row=0,column=0)


def main():
    """
        main function. Defines images, colours, window size and title.
    """

    global win,BACKGROUND1,BACKGROUND2,FOREGROUND1,my_img,my_img2,my_img3,my_img7

    win = Tk()
    win.title("Online Banking".center(100))
    win.minsize(2560,1600)
    #win.maxsize(1500,800)
    #win.state("zoomed")
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
    IMAGE7="images/logo7.png"


    TITLE="images/title.png"

    my_img=ImageTk.PhotoImage(Image.open(IMAGE6))# login page
    my_img2=ImageTk.PhotoImage(Image.open(IMAGE4),size=(1,1))# signup page
    my_img3=ImageTk.PhotoImage(Image.open(TITLE),size=(1,1))# py_bank
    my_img7=ImageTk.PhotoImage(Image.open(IMAGE7),size=(1,1))# logo for homepage

    login_page()

    win.mainloop()

if __name__=="__main__":
    main()
