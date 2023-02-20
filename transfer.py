import sqlite3
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

def transfer(info):
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
        if info[3]==user[6]:
            if user[9]>=info[1]:
                return True, -1, None
            else:
                return False, 1, "Insufficient balance"

def username_exists(receiver):
    """
        Checks if the username exists of recieving end.
    """
    all_client=DataActions.retrieve_all()
    for client in all_client:
        if client==receiver:
            return True, -1, None
    return False, 4, "username not found"



def main(info):
    """
        main function.
        Arguments:
            id : 0,
            balance : 1,
            date : 2,
            from_acc : 3,
            to_acc : 4,
            remarks : 5,
            status : 6
    """



try:
    configure()
except sqlite3.OperationalError:
    pass

if __name__=="__main__":
    pass
