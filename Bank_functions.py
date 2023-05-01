import mysql.connector
import random

conn= mysql.connector.connect(user = "root", database = "Bank_Data", password = "Hello1234")
cursor=conn.cursor(buffered=True)

def create_account(name, Acctype, dob, account_id):  
    addintobank = (f'INSERT INTO Bank_Data.CreatingAcc(name, Acctype, DOB, account_id, amount) VALUES("{name}",{Acctype},"{dob}",{account_id},{0.0})')
    cursor.execute(addintobank)
    conn.commit() 
    
def account_exists(account_id):
    print("ACCOUNT EXISTS")
    cursor.reset()
    cursor.execute(f"SELECT account_id FROM Bank_Data.CreatingAcc WHERE account_id ={account_id}")
    result = cursor.fetchone()
    print(result)
    conn.commit()
    return result is not None
    
def deposit_amount(account_id, amount):
    cursor.reset()
    cursor.execute(f'SELECT amount FROM Bank_Data.CreatingAcc WHERE account_id = {account_id}')
    cursor.execute(f"UPDATE Bank_Data.CreatingAcc SET amount = amount + {amount} WHERE account_id = {account_id}")
    print("Deposit amount: "+str(amount)+" into account ID "+str(account_id))
    conn.commit()
    
def withdraw_amount(account_id, amount):
    cursor.reset()
    cursor.execute(f"SELECT amount FROM Bank_Data.CreatingAcc WHERE account_id = {account_id}")
    current_balance = cursor.fetchone()[0]
    if amount > current_balance or amount < 0:
        print(f"Error: Insufficient balance for account_id {account_id}.")
    else:
        new_balance = current_balance - amount
        cursor.execute(f"UPDATE Bank_Data.CreatingAcc SET amount = {new_balance} WHERE account_id = {account_id}")
        print(f"Withdrew {amount} from account_id {account_id}. New balance is {new_balance}.")
    conn.commit()

        
def check_balance(account_id):
    cursor.reset()
    cursor.execute(f'SELECT amount FROM Bank_Data.CreatingAcc WHERE account_id ={account_id}')
    result_set = cursor.fetchall()
    if result_set:
        balance= result_set[0][0]
        print(f"amount for account_id {account_id}: {balance}")
    else:
        print(f"No account found with account_id {account_id}.")
    conn.commit()
            
def delete_data(account_id):
    cursor.reset()
    cursor.execute(f"SELECT amount FROM Bank_Data.CreatingAcc WHERE account_id = {account_id}")
    result = cursor.fetchone()
    if result is None:
        print("Account not found.")
    else:
        cursor.execute(f"DELETE FROM Bank_Data.CreatingAcc WHERE account_id = {account_id}")
        conn.commit()
        print(f"Account {account_id} deleted.")       
                    
