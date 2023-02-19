import sqlite3


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
        [('id', 'date', 'from_account', 'to_acc', 'remarks', 'status', oid)]
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
            date : 1,
            from_acc : 2,
            to_acc : 3,
            remarks : 4,
            status : 5
    """

    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()

    c.execute('INSERT INTO transaction VALUES (:id,:date,:from_acc,:to_acc,:remarks, :status)',{
        'id':info[0],
        'date':info[1],
        'from_acc':info[2],
        'to_acc':info[3],
        'remarks':info[4],
        'status':info[5]
    })
    print('amount transfered successfully')

    conn.commit()
    conn.close()

def main(info):
    """
        main function.
        Arguments:
            id : 0,
            date : 1,
            from_acc : 2,
            to_acc : 3,
            remarks : 4,
            status : 5
    """
    
try:
    configure()
except sqlite3.OperationalError:
    pass