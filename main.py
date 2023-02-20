from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import ImageTk,Image

import check_cred,DataActions,transfer


def login_page():
    """
        First login page
    """
    global login_frame,login_username,login_password,py_bank_logo,py_bank_title

    def clicked_signup():
        """
            Deletes login frame, py_bank title and calls sign_up function.
        """
        login_frame.grid_forget()
        py_bank_title.grid_forget()
        sign_up()

    py_bank_logo=Label(image=my_img,bg=BACKGROUND1)# Py Bank Logo
    py_bank_logo.grid(row=0,column=0,rowspan=19,ipady=400)

    py_bank_title=Label(image=my_img3,bg=BACKGROUND1)# Py Bank Text Image
    py_bank_title.grid(row=0,column=1,pady=(300,0))
    #Label(win,text="Py Bank",font=20,bg=BACKGROUND1,fg=FOREGROUND1).grid(row=0,column=2,pady=60)

    login_frame=LabelFrame(win,bg=BACKGROUND1,border=10,padx=100,pady=100)# contains username and password
    login_frame.grid(row=1,column=1)

    # Username 
    Label(login_frame,text="Username",bg=BACKGROUND1,fg=FOREGROUND1,font=15).grid(row=1,column=1,padx=30)
    login_username=Entry(login_frame,bg=BACKGROUND2,fg=FOREGROUND1)
    login_username.grid(row=1,column=2,padx=(0,80))
    
    # Password
    Label(login_frame,text="Password",bg=BACKGROUND1,fg=FOREGROUND1,font=15).grid(row=3,column=1,pady=(30,0))
    login_password=Entry(login_frame,show='*',bg=BACKGROUND2,fg=FOREGROUND1)
    login_password.grid(row=3,column=2,padx=(0,80),sticky="S")
    
    # Login Button
    Button(login_frame,text='Log In',command=login_check).grid(row=5,column=2,padx=(0,80),pady=30)

    Label(login_frame,text='OR',bg=BACKGROUND1,fg=FOREGROUND1).grid(row=6,column=2,padx=(0,80))
    Label(login_frame,text="Don't have an account?",bg=BACKGROUND1).grid(row=8,column=1,sticky='E')

    # Sign up Button
    Button(login_frame,text="Sign Up",command=clicked_signup).grid(row=8,column=2,pady=30,padx=(0,80))

def login_check():
    """
        Checks username and password
    """
    global logged_in_name,client_details

    try:# Removes any previous error if it's made 
        login_error1.grid_forget()
        login_error2.grid_forget()
    except NameError:
        pass
 
    all_clients=DataActions.retrieve_all()# gets all data from table Account

    for client in all_clients:# gets individual client details in format [('Fname', 'Mname', 'Lname', 'Email', 'dateOfBirth', 'Gender', 'Username', 'Password', 'balance', oid)]
        if login_username.get()==client[6]:# Checks if given username exits.
            if login_password.get()==client[7]:# Checks if username's password matches.
                """
                    Username and password matches so deletes login page and opens homepage.
                """
                login_frame.grid_forget()
                py_bank_logo.grid_forget()
                py_bank_title.grid_forget()
                logged_in_name=f"{client[0]} {client[2]}"
                homepage(client)    
            else:
                login_error_show(2)# Wrong password    
                return    
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

    global clicked_login,signup_frame,new_fname,new_lname,new_mname,new_email,new_dob,new_passwrd,new_cpasswrd,gvar,new_uname

    py_bank_title.grid(row=0,column=1,pady=(200,0))# places "Py Bank" title on top

    signup_frame=LabelFrame(win,bg=BACKGROUND1,border=10,padx=10,pady=10)# Frame for sign up data
    signup_frame.grid(row=1,column=1)

    def clicked_login():
        """
            Deletes sign_up frame, pybank title and logo. Then goes back to login page.
        """
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
    data_balance=100
    data_account_num=assign_acc()# Assigns account number 
    """
    Places all the data into a list.
    """
    all_data=[data_fname, data_mname, data_lname, data_email, data_dob, data_uname, data_passwrd, data_confpasswrd,data_gender]

    _check_data=check_cred.main(all_data)# checks for errors.
    # print(f'check : {_check_data}')

    if not _check_data[0]:# Error found
        signup_error_show(_check_data)# Shows respective error.

    else:# No error found.
        all_data.append(data_balance)# adds 100 at index 9
        all_data.append(data_account_num)#adds account number at index 10
        DataActions.signup_submit(all_data)# Adds data to Account table.
        messagebox.showinfo("Success","Submitted Sucessfully")
        clicked_login()
        
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

def assign_acc()->int:
    """
        Assigns Account number.
    """
    all_clients=DataActions.retrieve_all()
    try:
        return all_clients[-1][-2]+1
    except IndexError:
        return 90701000 

def homepage(client:list):
    """
        The homepage, after login is successfull.
    """

    #homepage_PybankLogo=Label(win,image=my_img7)# Py bank logo in home page at the top left corner.
    #homepage_PybankLogo.grid(row=0,column=0,rowspan=2)

    py_bank_logo.grid(row=0,column=0,rowspan=19,ipady=400)

    homepage_welcome_label=Label(win,text=f"Welcome {logged_in_name},".title(),font=30,bg=BACKGROUND1)# Welcome message at top.
    homepage_welcome_label.grid(row=0,column=1)

    homepage_frame1=LabelFrame(win,padx=20,pady=20,bg=BACKGROUND1)
    homepage_frame1.grid(row=2,column=1,sticky="S")
    Label(homepage_frame1,text="Account Number",bg=BACKGROUND1).grid(row=0,column=0)

    homepage_frame2=LabelFrame(win,padx=50,pady=10,bg=BACKGROUND1)# Account Number
    homepage_frame2.grid(row=3,column=1,sticky="N")
    Label(homepage_frame2,text=client[9],bg=BACKGROUND1).grid(row=0,column=0)

    homepage_frame3=LabelFrame(win,padx=20,pady=20,bg=BACKGROUND1)
    homepage_frame3.grid(row=2,column=2,sticky="S")
    Label(homepage_frame3,text="Account Balance",bg=BACKGROUND1).grid(row=0,column=0)

    homepage_frame4=LabelFrame(win,padx=60,pady=10,bg=BACKGROUND1)# Account Balance
    homepage_frame4.grid(row=3,column=2,sticky="N")
    homepage_balance=Label(homepage_frame4,text=f'Rs. {client[8]}',bg=BACKGROUND1)
    homepage_balance.grid(row=0,column=0)

    def clicked_refresh():
        """
            Refreshes account balance.
        """
        all_clients=DataActions.retrieve_all()
        for i in all_clients:
            if i[6]==client[6]:
                remove_homepage()
                homepage(i)

    homepage_refresh=Button(win,text="refresh",command=clicked_refresh)# Refresh button
    homepage_refresh.grid(row=1,column=1)

    homepage_frame5=LabelFrame(win,border=10,padx=50,pady=50,bg=BACKGROUND1)# Transaction Frame
    homepage_frame5.grid(row=5,column=1,padx=50,pady=50,columnspan=2)
    Label(homepage_frame5,text="Quick Fund Transfer",bg=BACKGROUND1).grid(row=0,column=0,columnspan=2,pady=(0,50))

    Label(homepage_frame5,text="To Account",bg=BACKGROUND1).grid(row=1,column=0)# To Account 
    homepage_toaccount=Entry(homepage_frame5)
    homepage_toaccount.grid(row=1,column=1,pady=(0,20))

    Label(homepage_frame5,text="Account Name",bg=BACKGROUND1).grid(row=2,column=0)# Account name
    homepage_accountname=Entry(homepage_frame5)
    homepage_accountname.grid(row=2,column=1,pady=(0,20))

    Label(homepage_frame5,text="Amount",bg=BACKGROUND1).grid(row=3,column=0)# Amount
    homepage_amount=Entry(homepage_frame5)
    homepage_amount.grid(row=3,column=1,pady=(0,20))

    Label(homepage_frame5,text="Remarks",bg=BACKGROUND1).grid(row=4,column=0)# Remarks
    homepage_remarks=Entry(homepage_frame5)
    homepage_remarks.grid(row=4,column=1)

    def clicked_transfer():
        transaction_info=['id 0','amount 1','date 2','from 3','to 4', 'uname 5','remark 6','status 7']
        transaction_info[1]=int(homepage_amount.get())
        transaction_info[3]=client[9]
        transaction_info[4]=int(homepage_toaccount.get())
        transaction_info[5]=homepage_accountname.get()
        transaction_info[6]=homepage_remarks.get()

        transfer.main(transaction_info)

        homepage_toaccount.delete(0,END)
        homepage_remarks.delete(0,END)
        homepage_accountname.delete(0,END)
        homepage_amount.delete(0,END)


    Button(homepage_frame5,text="transfer",command=clicked_transfer).grid(row=5,column=0,columnspan=2,pady=30)# transfer button

    """homepage_frame6=LabelFrame(win)# Load fund
    homepage_frame6.grid(row=7,column=2)

    Label(homepage_frame6,text="Load Fund").grid(row=0,column=0,columnspan=2)# Load fund title

    Label(homepage_frame6,text="Amount").grid(row=1,column=0)# Amount
    homepage_loadfund=Entry(homepage_frame6)
    homepage_loadfund.grid(row=1,column=1)

    def clicked_loadfund():
        amt=homepage_loadfund.get()
        homepage_loadfund.delete(0,END)
        tmp=list(client)
        tmp[8]+=int(amt)
        DataActions.edit(tmp)
        print('Amount added')

    Button(homepage_frame6,text="load",command=clicked_loadfund).grid(row=2,column=0,columnspan=2)# load button"""

    def clicked_signout():
        """
            Goes back to login page. 
        """
        remove_homepage()
        login_page()

        
    homepage_signout=Button(win,text='sign out',command=clicked_signout)
    homepage_signout.grid(row=10,column=1,pady=20,columnspan=2)

    def remove_homepage():
        """
            removes homepage. 
        """
        homepage_frame1.grid_forget()
        homepage_frame2.grid_forget()
        homepage_frame3.grid_forget()
        homepage_frame4.grid_forget()
        homepage_frame5.grid_forget()
        #homepage_frame6.grid_forget()

        homepage_refresh.grid_forget()
        homepage_welcome_label.grid_forget()
        py_bank_logo.grid_forget()
        homepage_signout.grid_forget()

    



def main():
    """
        main function. Defines images, colours, window size and title.
        Calls login page.
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

    my_img=ImageTk.PhotoImage(Image.open(IMAGE6))# login page
    my_img2=ImageTk.PhotoImage(Image.open(IMAGE4),size=(1,1))# signup page
    my_img3=ImageTk.PhotoImage(Image.open(TITLE),size=(1,1))# py_bank
    my_img7=ImageTk.PhotoImage(Image.open(IMAGE7),size=(1,1))# logo for homepage

    login_page()

    win.mainloop()# loops the window.

if __name__=="__main__":
    main()
