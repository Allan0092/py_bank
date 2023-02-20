from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
from PIL import ImageTk,Image

import check_cred,DataActions


def login_page():
    """
        First login page
    """
    global login_frame,login_username,login_password,py_bank_logo,py_bank_title

    def clicked_signup():
        """
            Deletes login login_frame, py_bank title and calls sign_up function.
        """        
        login_frame.grid_forget()
        py_bank_title.grid_forget()
        sign_up()

    py_bank_logo=Label(image=my_img,bg=BACKGROUND1)
    py_bank_logo.grid(row=0,column=0,rowspan=19,ipady=200)# Py Bank Logo

    py_bank_title=Label(image=my_img3,bg=BACKGROUND1)
    py_bank_title.grid(row=0,column=1,pady=(100,0))# Py Bank Text Image
    #Label(win,text="Py Bank",font=20,bg=BACKGROUND1,fg=FOREGROUND1).grid(row=0,column=2,pady=60)

    login_frame=Label(win,bg=BACKGROUND1,border=10,padx=50,pady=50)
    login_frame.grid(row=1,column=1)

    # Username 
    Label(login_frame,text="Username:",bg=BACKGROUND1,fg=FOREGROUND1,font=15).grid(row=1,column=1,pady=30,padx=30)
    login_username=Entry(login_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    login_username.grid(row=1,column=2,padx=(0,80))
    
    # Password
    Label(login_frame,text="Password:",bg=BACKGROUND1,fg=FOREGROUND1,font=15).grid(row=2,column=1)
    login_password=Entry(login_frame,show='*',bg=BACKGROUND2,fg=FOREGROUND1)
    login_password.grid(row=2,column=2,padx=(0,80))
    
    # Login Button    
    Button(login_frame,text='Log In',font=80,activebackground="green",command=login_check).grid(row=3,column=2,padx=(0,80),pady=30)
    Label(login_frame,text='OR',bg=BACKGROUND1,fg=FOREGROUND1,font=50).grid(row=4,column=2,padx=(0,80))

    # Sign up Button
    Label(login_frame,text="Don't have a account?",bg="#90cad1",fg="black",font=20).grid(row=5,column=1,padx=(0,0),sticky="E")
    Button(login_frame,text="Sign Up",command=clicked_signup,font=60,activebackground="red").grid(row=5,column=2,pady=30,padx=(0,80))

def login_check():
    """
        Checks username and password
    """
    global logged_in_name

    try:# Removes any previous error if it's made 
        login_error1.grid_forget()
        login_error2.grid_forget()
    except NameError:
        pass

    all_clients=DataActions.retrieve_all()# gets all data from table Account

    for client in all_clients:# gets individual client details in format [('Fname', 'Mname', 'Lname', 'Email', 'dateOfBirth', 'Gender', 'Username', 'Password', oid)]
        if login_username.get()==client[6]:# Checks if given username exits.
            if login_password.get()==client[7]:# Checks if username's password matches.
                """
                    Username and password matches so deletes login page and opens homepage.
                """
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

    if what==1:# shows "Username not found"
        login_error1.grid(row=2,column=2,sticky="WN")
    elif what==2:# shows "Password is incorrect"
        login_error2.grid(row=4, column=2,sticky="WN")


def sign_up():
    """
        sign up page
    """

    global signup_frame,new_fname,new_lname,new_mname,new_email,new_dob,new_passwrd,new_cpasswrd,gvar,new_uname

    #py_bank_title.grid(row=0,column=1,pady=(200,0))# places "Py Bank" title on top
   
    signup_frame=LabelFrame(win,bg=BACKGROUND1,border=3,padx=10,pady=10)
    signup_frame.grid(row=1,column=1)

    def clicked_login():
        """
            Deletes sign_up frame, pybank title and logo. Then goes back to login page.
        """        
        signup_frame.grid_forget()
        py_bank_title.grid_forget()
        login_page()

    gvals=[
        ("Male",'male'),
        ("Female",'female'),
        ("Other",'other')
    ]
    gvar=StringVar(signup_frame,'None')


    Label(signup_frame,image=my_img2,bg=BACKGROUND1).grid(row=0,column=0,pady=(10,0))

    Label(signup_frame,text="Sign up",font=200,bg='#90cad1',fg=FOREGROUND1).grid(row=0,column=1,pady=(0,10),sticky="W")

    Label(signup_frame,text='            First name:',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=2,column=0)
    new_fname=Entry(signup_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    new_fname.grid(row=2,column=1,padx=(0,100))

    Label(signup_frame,text='        Middle name:',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=4,column=0)
    new_mname=Entry(signup_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    new_mname.grid(row=4,column=1,pady=30,padx=(0,100))

    Label(signup_frame,text='            Last name:',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=6,column=0)
    new_lname=Entry(signup_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    new_lname.grid(row=6,column=1,padx=(0,100))

    Label(signup_frame,text='            Email Id:',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=8,column=0)
    new_email=Entry(signup_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    new_email.grid(row=8,column=1,pady=(30,0),padx=(0,100))

    Label(signup_frame,text='      Date of Birth:',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=10,column=0)
    new_dob=DateEntry(signup_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    new_dob.grid(row=10,column=1,ipadx=40,sticky="W",pady=(20,0))

    Label(signup_frame,text='Gender:    ',bg='#90cad1',fg=FOREGROUND1).grid(row=12,column=0,pady=(30,0),sticky='E')
    _rowcnt=12
    for text,mode in gvals:
        Radiobutton(signup_frame,fg=FOREGROUND1,bg='#90cad1',text=text,variable=gvar, value=mode).grid(row=_rowcnt,column=1,sticky='WS',pady=5)
        _rowcnt+=1

    Label(signup_frame,text="             Username:",bg=BACKGROUND1,fg=FOREGROUND1).grid(row=16,column=0,pady=(40,0))
    new_uname=Entry(signup_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    new_uname.grid(row=16,column=1,sticky='W',pady=(40,0))

    Label(signup_frame,text='            Password:',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=18,column=0,pady=(40,0))
    new_passwrd=Entry(signup_frame,show='*',bg=BACKGROUND2,fg=FOREGROUND1)
    new_passwrd.grid(row=18,column=1,padx=(0,100),pady=(40,0))

    Label(signup_frame,text='Confirm Password:',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=20,column=0,pady=(40,10))
    new_cpasswrd=Entry(signup_frame,show='*',bg=BACKGROUND2,fg=FOREGROUND1)
    new_cpasswrd.grid(row=20,column=1,pady=(40,0),padx=(0,100))
    
    Button(signup_frame,text='Submit',font=80,bg=BACKGROUND2,fg=FOREGROUND1,command=sign_up_data,activebackground="green").grid(row=22,column=1,pady=10,padx=(0,100))

    Label(signup_frame,text='OR',bg=BACKGROUND1,font=50).grid(row=23, column=1,padx=(0,100),pady=5)
    Button(signup_frame,text='Log in',bg=BACKGROUND2,fg=FOREGROUND1,command=clicked_login,font=80).grid(row=24,column=1,pady=(0,20),padx=(0,100))

def sign_up_data():
    """
        Processes all data from sign up page, then checks for errors and finnally submits data into Account table.
    """
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
    """
    Places all the data into a list.
    """
    all_data=[data_fname, data_mname, data_lname, data_email, data_dob, data_uname, data_passwrd, data_confpasswrd,data_gender]

    _check_data=check_cred.main(all_data)# checks for errors.
    # print(f'check : {_check_data}')

    if not _check_data[0]:# Error found
        signup_error_show(_check_data)# Shows respective error.

    else:# No error found.
        DataActions.signup_submit(all_data)# Adds data to Account table.
        messagebox.showinfo("Success","Submitted Sucessfully")
        
def signup_error_show(_where:list) -> None:
    """
        displays the error message at sign up page
        Arguement:
            _where:list
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

    try:# removes any previous error in sign up page.
        signup_error1.grid_forget()
    except NameError:
        pass

    _row=error_codes[_where[1]][2]
    _text=error_codes[_where[1]][1]
    # print(f'\nError : {_text}\nat {_row}')

    signup_error1=Label(signup_frame,text=_text + _where[2],fg='red',bg=BACKGROUND1)# error in sign up page
    signup_error1.grid(row=_row,column=1,columnspan=4,sticky='WN')

def homepage():
    """
        The homepage, after login is successfull.
    """

    homepage_PybankLogo=Label(win,image=my_img7)# Py bank logo in home page at the top left corner.
    homepage_PybankLogo.grid(row=0,column=0,rowspan=3)

    Label(win,text=f"Welcome {logged_in_name},").grid(row=0,column=1)# Welcome message at top.

    homepage_frame1=LabelFrame(win)
    homepage_frame1.grid(row=1,column=1)
    Label(homepage_frame1,text="Account username").grid(row=0,column=0)

    homepage_frame2=LabelFrame(win,borderwidth=5)
    homepage_frame2.grid(row=2,column=1,sticky="N")
    Label(homepage_frame2,text='XXXXXXXXXX').grid(row=0,column=0)

    homepage_frame3=LabelFrame(win)
    homepage_frame3.grid(row=1,column=2)
    Label(homepage_frame3,text="Account Balance").grid(row=0,column=0)

    homepage_frame4=LabelFrame(win)
    homepage_frame4.grid(row=2,column=2,sticky="N")
    Label(homepage_frame4,text='20,000').grid(row=0,column=0)

    Button(win,text="refresh").grid(row=1,column=3)# Refreah button

    homepage_frame5=LabelFrame(win)# Transaction Frame
    homepage_frame5.grid(row=3,column=2)
    Label(homepage_frame5,text="Quick Fund Transfer").grid(row=0,column=0,columnspan=2)

    Label(homepage_frame5,text="To Account").grid(row=1,column=0)# To Account 
    homepage_toaccount=Entry(homepage_frame5)
    homepage_toaccount.grid(row=1,column=1)

    Label(homepage_frame5,text="Account Name").grid(row=2,column=0)# Account name
    homepage_accountname=Entry(homepage_frame5)
    homepage_accountname.grid(row=2,column=1)

    Label(homepage_frame5,text="Amount").grid(row=3,column=0)# Amount
    homepage_amount=Entry(homepage_frame5)
    homepage_amount.grid(row=3,column=1)

    Label(homepage_frame5,text="Remarks").grid(row=4,column=0)# Remarks
    homepage_remarks=Entry(homepage_frame5)
    homepage_remarks.grid(row=4,column=1)

    Button(homepage_frame5,text="transfer").grid(row=5,column=0,columnspan=2)# transfer button

    homepage_frame6=LabelFrame(win)# Load fund
    homepage_frame6.grid(row=4,column=2)

    Label(homepage_frame6,text="Load Fund").grid(row=0,column=0,columnspan=2)# Load fund title

    Label(homepage_frame6,text="Amount").grid(row=1,column=0)# Amount
    homepage_loadfund=Entry(homepage_frame6)
    homepage_loadfund.grid(row=1,column=1)

    Button(homepage_frame6,text="load").grid(row=2,column=0,columnspan=2)# load button

    Button(win,text='sign out').grid(row=4,column=3)



def main():
    """
        main function. Defines images, colours, window size and title.
        Calls login page.
    """

    global win,BACKGROUND1,BACKGROUND2,FOREGROUND1,my_img,my_img2,my_img3,my_img7

    win = Tk()
    win.title("Online Banking".center(100))
    #win.minsize(2560,1600)
    #win.maxsize(1500,800)
    win.state("zoomed")
    BACKGROUND1="#90cad1"
    BACKGROUND2="white"
    FOREGROUND1='black'
    win.config(background=BACKGROUND1)
    """
    Path for all images used.
    """
    IMAGE="images/logo"
    IMAGE2="images/logo2"
    IMAGE3="images/logo3.png"
    IMAGE4="images/logo4c.png"
    IMAGE5="images/logo5.png"
    IMAGE6="images/logo6.png"
    IMAGE7="images/logo7.png"


    TITLE="images/title.png"# Py Bank title

    my_img=ImageTk.PhotoImage(Image.open(IMAGE7))# login page
    my_img2=ImageTk.PhotoImage(Image.open(IMAGE4),size=(1,1))# signup page
    my_img3=ImageTk.PhotoImage(Image.open(TITLE),size=(1,1))# py_bank
    my_img7=ImageTk.PhotoImage(Image.open(IMAGE7),size=(1,1))# logo for homepage

    login_page()

    win.mainloop()# loops the window.

if __name__=="__main__":
    main()
    