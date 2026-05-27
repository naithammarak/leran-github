
import sqlite3
import sys
from datetime import datetime

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
# creat table when no file

def init_db():
    conn = sqlite3.connect("wallet.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            note TEXT
            )''')
    conn.commit()
    conn.close()
    print("system :  data is saved")


# add transaction


def add_transaction(t_type,amount,category,note=""):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions(type,amount,category,date,note) VALUES(?,?,?,?,?)
    ''',(t_type,amount,category,current_time,note))
    conn.commit()
    conn.close()

    print('transactions have saved')


def view_transaction():
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM transactions''')
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    
    conn.close()

def get_balance():
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT type,amount FROM transactions''')
    rows = cursor.fetchall()
    total_income = 0.0
    total_expense = 0.0

    for row in rows:
        if row[0] == "income":
            total_income += row[1]
        elif row[0] == "expense":
            total_expense += row[1]

    conn.close()
    
    total_balance = total_income - total_expense
    

    return total_balance




if __name__ == '__main__':
    init_db()
    
    while True:
        print('wellcome to wallet app')
        print('1.add transaction ')
        print('2.view transaction')
        print('3.get balance')
        print('4.exit')
        try:
            choice = input('please choice 1-4: ')
        except:
            print('invalid input please choose between 1-4 ')
            continue

        if choice == "1":
            
            while True:
                t_type = input('income or expense: ')

                if t_type == "income" or t_type == "expense":
                    break
                else:
                    print("invalid input")
            while True:
                try:
                    amount = float(input("enter amount: "))
                except:
                    print("invalid input")
                    continue
                if amount > 0:
                    break
                else:
                    print("amount must be grater than 0")
                    
            

            
            category = input('enter category: ')
            note = input("note: ")

            add_transaction(t_type,amount,category,note)

        elif choice == "2":
            view_transaction()
        elif choice == "3":
            print("the total balance is : ",get_balance())


        elif choice == "4":
            break
        


            
            
        
