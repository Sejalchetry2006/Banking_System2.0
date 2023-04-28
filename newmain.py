import mysql.connector
import random
##from Bank_functions import BankFunctions
conn= mysql.connector.connect(user = "root", database = "Bank_Data", password = "Hello1234")
cursor=conn.cursor()
def create_account():
    print("1. Checking account")
    print("2. Savings account")
    print("3. Both")
    Acctype = input("Choose the series of numbers which will determine the account type: ")
    Accountcreate=False
    if Acctype in ['1', '2', '3']:
        name = input("Enter name: ")
        dob = input("Enter DOB (YYYY-MM-DD): ")
        account_id = ''.join([str(random.randint(0,9)) for i in range(7)])
        print("Account name: " + name)
        print("Account type: " + Acctype)
        print("Date of birth: " + dob)
        print("Account ID: " + account_id)
        Accountcreate=True
        if(Accountcreate==True):
            pinnum=int(input("Enter pin number(4 Digit): "))
            pinnum2=int(input("Enter pin again: "))
            if(pinnum==pinnum2):
              Accountcreate==False
            elif(pinnum!=pinnum2):
                pinnum2=int(input("PIN does not match, try again"))
            else:
                print("Invalid account type")
                create_account()
            
        addintobank='INSERT INTO Bank_Data.CreatingAcc(name, Acctype, DOB, account_id) VALUES("'+name+'", "'+Acctype+'", '+dob+', '+account_id+')'
        cursor.execute(addintobank)
        conn.commit()
create_account()
def deposit(account_id, amount):
    account_id=int(input("Enter account ID:"))
    amount=int(input("Enter amount number:"))
    cursor.execute(account_id, amount)
    print("Deposit amount:"+amount+"into account ID"+account_id)
    conn.commit()
   
def withdraw(account_id, amount):
    cursor.execute('SELECT balance FROM account WHERE id = %s', (account_id,))
    current_balance = cursor.fetchone()[0]
    amount=int(input("Emter amount you want to withdraw:"))
    if current_balance < amount:
        print(f"Error: Insufficient balance for account ID {account_id}.")
        return
    new_balance = current_balance - amount
    cursor.execute('UPDATE accounts SET balance = %s WHERE id = %s', (new_balance, account_id))
    print(f"Withdrew {amount} from account ID {account_id}. New balance is {new_balance}.")
    conn.commit()
    
def check_balance(account_id):
    account_id=int(input("Enter account id:"))
    cursor.execute('SELECT balance FROM accounts WHERE id = %s', (account_id,))
    result_set = cursor._rows
    if result_set:
        balance = result_set[0][0]
        print(f"Balance for account ID {account_id}: {balance}")
    else:
        print(f"No account found with ID {account_id}.")
        conn.commit()

def delete_data():
    account_id=cursor.fetchall()
    for i in account_id:
        if account_id.count(i)>1:
            for j in range(account_id.count(i)-1):
               account_id.remove(i) 
    cursor.execute(f'DELETE Bank_system.CreatingAcc FROM account_id WHERE id = %s', (account_id,))

            
                   