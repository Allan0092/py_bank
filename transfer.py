import sqlite3
from datetime import datetime
import DataActions


DATABASE="bank_data.db"

def configure():
    '''
        creates transaction table.
    '''
    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()

    c.execute("""
    create table transaction(
        id text,
        amount integer,
        date text,
        from_acc text,
        to_acc text,
        remarks text,
        status text
    )
    """)
    print("database created successfully")
    conn.commit()
    conn.close()

def retrieve_all():
    """
        retrieves all data in the form of a list.
        [('id', 'amount', 'date', 'from_account', 'to_acc', 'remarks', 'status', oid)]
    """
    conn= sqlite3.connect(DATABASE)

    c= conn.cursor()

    c.execute("SELECT *, oid FROM transaction")

    records= c.fetchall()#[(),()]

    return records

    conn.close()

def save_transfer(info):
    """
        Adds a transaction.
        Arguments:
            id : 0,
            amount : 1,
            date : 2,
            from_acc : 3,
            to_acc : 4,
            remarks : 5,
            status : 6
    """

    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()

    c.execute('INSERT INTO transaction VALUES (:id, :amount, :date, :from_acc, :to_acc, :remarks, :status)',{
        'id':info[0],
        'amount':info[1],
        'date':info[2],
        'from_acc':info[3],
        'to_acc':info[4],
        'remarks':info[5],
        'status':info[6]
    })
    print('amount transfered successfully')

    conn.commit()
    conn.close()

def enough_balance(info):
    """
        checks if account has enough balance.
        Arguments:
            id : 0,
            amount : 1,
            date : 2,
            from_acc : 3,
            to_acc : 4,
            remarks : 5,
            status : 6
    """

    all_users=DataActions.retrieve_all()
    
    for user in all_users:
        if info[3]==user[9]:
            if user[8]>=info[1]:
                return True, -1, None
            else:
                return False, 1, "Insufficient balance"
    return

def account_exists(receiver_num,receiver_uname):
    """
        Checks if the account number exists of recieving end.
    """
    all_client=DataActions.retrieve_all()
    for client in all_client:
        if client[9]==receiver_num:
            if client[6]==receiver_uname:
                return True, -1, None

    return False, 4, "account not found"

def new_transaction_id():
    """
        Creates a unique transfer id.
    """
    try:
        all_transactions=retrieve_all()
    except sqlite3.OperationalError:
        all_transactions=[()]

    try:
        return all_transactions[-1][-2]+1
    except IndexError:
        return 4201000 

def withdraw(accnumber,amt):
    """
        Deducts amount from account.
        Arguments:
            accnumber : int
            amt : int
    """

    all_clients=DataActions.retrieve_all()
    for c in all_clients:
        if c[9]==accnumber:
            c_list=list(c)
            c_list[8]-=amt
            DataActions.edit(c_list)

def deposit(accnumber,amt):
    """
        Adds balance to account.
    """

    all_clients=DataActions.retrieve_all()
    for c in all_clients:
        if c[9]==accnumber:
            c_list=list(c)
            c_list[8]+=amt
            DataActions.edit(c_list)

def main(info):
    """
        main function.
        Arguments:
            id : 0,
            amount : 1,
            date : 2,
            from_acc : 3,
            to_acc : 4,
            acc_name : 5,
            remarks : 6,
            status : 7
    """
    check1=account_exists(info[4],info[5])
    if check1[0]:
        check2=enough_balance(info)
        if check2[0]:
            info[0]=new_transaction_id()
            info[2]=datetime.today().strftime('%Y-%m-%d')
            info[7]='complete'
            withdraw(info[3],info[1])
            deposit(info[4],info[1])
            #save_transfer(info)
            print("Done")
        else:
            print(check2)
    else:
        print(check1)


try:
    configure()
except sqlite3.OperationalError:
    pass

if __name__=="__main__":
    pass