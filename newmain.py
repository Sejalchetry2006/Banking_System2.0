import mysql.connector
import random
from Bank_functions import BankFunctions
conn= mysql.connector.connect(user = "root", database = "Bank_system", password = "Hello1234")
cursor=conn.cursor()
def create_account():
  print("1.Checking account") 
  print("2.Savings account") 
  print("3.Both")
  Acctype=input("Choose the seres of numbers which will deterime the account type")
  if(Acctype==1 or 2 or 3):
      name=input("Enter name")
      DOB=int(input("Enter DOB:"))
      for i in range(8):
          account_id=random.randit(1,10)
      print("Account name:"+name)
      print("Account type"+ Acctype)
      print("Date of birth:"+DOB)
      print("Account number:"+account_id)
      addintobak='INSERT INTO Bank_system.CreatingAcc(name, Acctype, DOB, account_id) VALUES("'+name+'", "'+Acctype+'", '+DOB+', '+account_id+')'
      cursor.execute(account_id, Acctype, DOB, account_id)
      conn.commit()
create_account()
      
def deposit(account_id, amount):
    account_id=int(input("Enter account ID:"))
    amount=int(input("Enter amount number:"))
    cursor.execute(account_id, amount)
    print("Deposit amount:"+amount+"into account ID"+account_id)
    conn.commit()
   
def withdraw(account_id, amount):
    cursor.execute('SELECT balance FROM accounts WHERE id = %s', (account_id,))
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



        


        

