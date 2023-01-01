import sqlite3

if __name__=="__main__":
    database=sqlite3.connect("bank_data.db")
    comms=database.cursor()

    comms.execute("""


    """)
