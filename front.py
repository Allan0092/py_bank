from tkinter import *
from PIL import ImageTk,Image
import sql_thngs


win = Tk()
win.title("Online Banking".center(100))
win.minsize(800,700)
win.maxsize(1200,900)
win.config(background="white")

IMAGE="/home/gtm/Documents/projects/beta-bank/logo2"
my_img=ImageTk.PhotoImage(Image.open(IMAGE),size=(10,10))
my_imag=Label(image=my_img)



def start_page():
    my_imag.place(x=20,y=0)
    text_welcome=Label(win, text="Welcome To The Number One Bank In The World!!",font=10,bg="white")
    text_welcome.grid(row=0,column=1,padx=100,pady=100)
    
    login_page()
    
    login_button=Button(win, text="Log in",command=login_page,highlightcolor='red').grid(row=10,column=1,padx=50,pady=20)
    signup_button=Button(win,text="Sign up",command=signup_page).grid(row=11,column=1,padx=50,pady=20)
    

def signup_page():
    win1=Toplevel(win)
    win1.title("Registration")
    win1.minsize(500,800)
    win1.maxsize(1200,900)
    win1.config(background="white")

    Label(win1,text="Welcome To The Number One Bank In The World!!",font=10,bg="white").grid(row=0,column=1,padx=100,pady=100)
    text_fname=Label(win1,text="First Name",bg="white").place(x=170,y=260)
    text_lname=Label(win1,text="Last Name",bg="white").place(x=170,y=310)
    text_email=Label(win1,text="Email",bg="white").place(x=235,y=375)
    text_password=Label(win1,text="Password",bg="white").place(x=185,y=440)
    text_confPass=Label(win1,text="Confirm Password",bg="white").place(x=80,y=515)

    insert_fname=Entry(win1,borderwidth=5)
    #insert_fname.insert(0,"First Name")
    insert_fname.grid(row=1,column=1)
    
    insert_lname=Entry(win1,borderwidth=5)
    #insert_lname.insert(0,"Last Name")
    insert_lname.grid(row=2,column=1)

    insert_lname.grid(row=4,column=1,pady=10)
    insert_pass=Entry(win1,borderwidth=5,show='*').grid(row=5,column=1,pady=10)
    insert_conf_pass=Entry(win1,borderwidth=5,show='*').grid(row=6,column=1,pady=10)

    insert_email=Entry(win1,borderwidth=5)

    #insert_email.insert(0,"example@email.com")
    insert_email.grid(row=3,column=1,pady=10)

    submit_button=Button(win1, text="submit").grid(row=10,column=1,padx=50,pady=20)
    

def login_page():
    text_username=Label(win,text="username",bg="white").place(x=180,y=260)
    text_password=Label(win,text="password",bg="white").place(x=180,y=310)

    insert_username=Entry(win,borderwidth=5)
    #insert_username.insert(0,"Username")
    insert_username.grid(row=1,column=1)

    insert_password=Entry(win,borderwidth=5,show='*')
    #insert_password.insert(0,"Password")
    insert_password.grid(row=2,column=1)

    

start_page()


win.mainloop()