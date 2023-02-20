import sqlite3


DATABASE="bank_data.db"

def configure() -> None:
    '''
        execute if table is not created.
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

def signup_submit(info:list) -> None:
    """
        submits data from sign up page into database.
        Arguments:
            first_name : 0,
            middle_name : 1,
            last_name : 2,
            email : 3,
            dob : 4,
            username : 5,
            password : 6,
            gender : 8,
            balance : 9,
            account number : 10
    """

    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()

    c.execute('INSERT INTO Account VALUES (:first_name,:middle_name,:last_name,:email,:dob, :gender, :username, :password, :balance)',{
        'first_name':info[0],
        'middle_name':info[1],
        'last_name':info[2],
        'email':info[3],
        'dob':info[4],
        'gender':info[8],
        'username':info[5],
        'password':info[6],
        'balance':info[9],
        'accnumber':info[10]

    })
    print('data submitted successfully')

    conn.commit()
    conn.close()

def retrieve_all() -> list:
    """
        retrieves all data in form of a list.
        [('Fname', 'Mname', 'Lname', 'Email', 'dateOfBirth', 'Gender', 'Username', 'Password', 'balance','account number', oid)]
    """
    conn= sqlite3.connect(DATABASE)

    c= conn.cursor()

    c.execute("SELECT *, oid FROM Account")

    records= c.fetchall()#[(),()]

    return records

    conn.close()

try:# Creates tables for new host machine.
    configure()
except sqlite3.OperationalError:
    pass

