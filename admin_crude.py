import sqlite3
from tkinter import *
from tkinter import messagebox
from main import assign_acc

DATABASE="bank_data.db"

def configure():
    '''
        execute if table not created.
    '''
    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()

    c.execute("""
    create table Account(
        first_name text,
        middle_name text,
        last_name text,
        email text,
        dob text,
        gender text,
        username text,
        password text,
        balance integer,
        accnumber integer

    )
    """)
    print("database created successfully")
    conn.commit()
    conn.close()

def main():
    global win,fname,mname,lname,email,dob,gender,uname,passwrd,update_box,delete_box

    try:
        configure()
    except sqlite3.OperationalError:
        pass

    win=Tk()
    win.title("Bank")
    win.minsize(700,1000)

    Label(win,text="first name").grid(row=0,column=0)
    fname=Entry(win)
    fname.grid(row=0,column=1)

    Label(win,text="middle name").grid(row=1,column=0)
    mname=Entry(win)
    mname.grid(row=1,column=1,pady=10)

    Label(win,text="last name").grid(row=2,column=0)
    lname=Entry(win)
    lname.grid(row=2,column=1,pady=10)

    Label(win,text="email").grid(row=3,column=0)
    email=Entry(win)
    email.grid(row=3,column=1,pady=10)

    Label(win,text="dob").grid(row=4,column=0)
    dob=Entry(win)
    dob.grid(row=4,column=1,pady=10)

    Label(win,text="gender").grid(row=5,column=0)
    gender=Entry(win)
    gender.grid(row=5,column=1,pady=10)

    Label(win,text="Username").grid(row=6,column=0,padx=(50,0))
    uname=Entry(win)
    uname.grid(row=6,column=1,pady=10)

    Label(win,text="password").grid(row=7,column=0)
    passwrd=Entry(win)
    passwrd.grid(row=7,column=1,pady=10)

    Button(win,text="Submit",command=submit).grid(row=8,column=1,pady=10)

    Button(win,text='All Clients',command=query).grid(row=20,column=1,pady=(20,50))

    Label(win,text='Update ID').grid(row=21,column=0)
    update_box=Entry(win)
    update_box.grid(row=21,column=1)
    Button(win,text="Update",command=edit).grid(row=22,column=1,pady=(10,50))

    Label(win,text='Delete ID').grid(row=23,column=0)
    delete_box=Entry(win)
    delete_box.grid(row=23,column=1)
    Button(win,text="Delete",command=delete).grid(row=24,column=1,pady=(10,0))

    win.mainloop()

def submit():
    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()

    c.execute('INSERT INTO Account VALUES (:first_name,:middle_name,:last_name,:email,:dob, :gender, :username, :passwrd, :balance, :accnumber)',{
        'first_name':fname.get(),
        'middle_name':mname.get(),
        'last_name':lname.get(),
        'email':email.get(),
        'dob':dob.get(),
        'gender':gender.get(),
        'username':uname.get(),
        'passwrd':passwrd.get(),
        'balance':0,
        'accnumber': assign_acc()
    })
    print('data submitted successfully')

    uname.delete(0,END)
    fname.delete(0,END)
    lname.delete(0,END)
    mname.delete(0,END)
    passwrd.delete(0,END)
    email.delete(0,END)
    dob.delete(0,END)
    gender.delete(0,END)
    passwrd.delete(0,END)

    conn.commit()
    conn.close()

def query():

    conn= sqlite3.connect(DATABASE)

    c= conn.cursor()

    c.execute("SELECT *, oid FROM Account")

    records= c.fetchall()
    print(records)

    print_record=''
    for record in records:
        print_record += str(record[6])+'  ' +str(record[3])+' '+'\t'+str(record[7])+"\n"

    query_label= Label(win,text= print_record)
    query_label.grid(row=9, column=0, columnspan=4)

    conn.commit()
    conn.close()

def edit():

    global win2,fname_edit,mname_edit,lname_edit,uname_edit,email_edit,dob_edit,gender_edit,passwrd_edit,balance_edit,number_edit


    win2= Toplevel(win)
    win2.title('Update Data')
    win2.geometry('800x800')

    conn= sqlite3.connect(DATABASE)

    c=conn.cursor()

    record_id= update_box.get()

    c.execute('SELECT * FROM Account WHERE oid='+ record_id)

    records = c.fetchall()

    # print(records)

    Label(win2,text="first name").grid(row=0,column=0)
    fname_edit=Entry(win2)
    fname_edit.grid(row=0,column=1)

    Label(win2,text="middle name").grid(row=1,column=0)
    mname_edit=Entry(win2)
    mname_edit.grid(row=1,column=1,pady=10)

    Label(win2,text="last name").grid(row=2,column=0)
    lname_edit=Entry(win2)
    lname_edit.grid(row=2,column=1,pady=10)

    Label(win2,text="email").grid(row=3,column=0)
    email_edit=Entry(win2)
    email_edit.grid(row=3,column=1,pady=10)

    Label(win,text="dob").grid(row=4,column=0)
    dob_edit=Entry(win)
    dob_edit.grid(row=4,column=1,pady=10)

    Label(win2,text="gender").grid(row=5,column=0)
    gender_edit=Entry(win2)
    gender_edit.grid(row=5,column=1,pady=10)

    Label(win2,text="Username").grid(row=6,column=0,padx=(50,0))
    uname_edit=Entry(win2)
    uname_edit.grid(row=6,column=1,pady=10)

    Label(win2,text="password").grid(row=7,column=0)
    passwrd_edit=Entry(win2)
    passwrd_edit.grid(row=7,column=1,pady=10)

    Label(win2,text="Balance").grid(row=8,column=0)
    balance_edit=Entry(win2)
    balance_edit.grid(row=8,column=1)

    Label(win2,text="Account number").grid(row=9,column=0)
    number_edit=Entry(win2)
    number_edit.grid(row=9,column=1)


    Button(win2,text="Update",command=update).grid(row=11,column=1,pady=10)


    for record in records:
        fname_edit.insert(0,record[0])
        mname_edit.insert(0,record[1])
        lname_edit.insert(0,record[2])
        email_edit.insert(0,record[3])
        dob_edit.insert(0,record[4])
        gender_edit.insert(0,record[5])
        uname_edit.insert(0,record[6])
        passwrd_edit.insert(0,record[7])
        balance_edit.insert(0,record[8])
        number_edit.insert(0,record[9])


    conn.commit()
    conn.close()

def update():
    conn= sqlite3.connect(DATABASE)

    c= conn.cursor()

    c.execute("""UPDATE Account SET
        first_name= :fname,
        middle_name= :mname,
        last_name= :lname,
        email= :email,
        dob= :dob,
        gender= :gender,
        username= :uname,
        password=:passwrd,
        balance=:balance,
        accnumber=:accnumber
        WHERE oid= :oid""",{
        'fname':fname_edit.get(),
        'mname':mname_edit.get(),
        'lname':lname_edit.get(),
        'email':email_edit.get(),
        'dob':dob.get(),
        'gender':gender_edit.get(),
        'uname':uname_edit.get(),
        'passwrd':passwrd_edit.get(),
        'balance':balance_edit.get(),
        'accnumber':number_edit.get(),
        'oid':update_box.get()
    })
    conn.commit()
    conn.close()
    win2.destroy()

def delete():
    conn= sqlite3.connect(DATABASE)

    c= conn.cursor()

    c.execute("DELETE from Account WHERE oid = " + delete_box.get())
    print('Delete Sucessfully')

    c.execute("SELECT *, oid FROM Account")

    records= c.fetchall()
    print(records)

    print_record=''
    for record in records:
        print_record += str(record[0])+' '+str(record[1])+' '+'\t'+str(record[4])+"\n"

    query_label= Label(win,text= print_record)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()

    messagebox.showinfo("Alert","Deleted Sucessfully")

def drop_acc():
    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()

    c.execute("DROP TABLE Account;")

    conn.commit()
    conn.close()

def drop_transaction():
    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()

    c.execute("DROP TABLE transaction;")

    conn.commit()
    conn.close()

if __name__=="__main__":
    main()



