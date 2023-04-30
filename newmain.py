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

def account_exists(account_id):
    print("ACCOUNT EXISTS")
    cursor.reset()
    cursor.execute("SELECT account_id FROM Bank_Data.CreatingAcc WHERE account_id = %s",(account_id,))
    result = cursor.fetchone()
    print(result)
    conn.commit()
    return result is not None
    
def deposit_amount():
    print("DEPOSIT AMOUNT")
    cursor.reset()
    account_id=int(input("Enter account ID:"))
    if(account_exists(account_id)):
     amount=int(input("Enter amount number:"))
     cursor.execute(f"SELECT account_id FROM Bank_Data.CreatingAcc WHERE account_id = {account_id}")
     cursor.reset()
     cursor.execute (f"UPDATE Bank_Data.CreatingAcc SET amount={amount} WHERE account_id={amount}")
     print("Deposit amount:"+str(amount)+"into account ID"+str(account_id))
    else:
        print("Account not found, try agian")
        deposit_amount()
    conn.commit()
deposit_amount()
def withdraw_amount():
       cursor.reset()
       print("WITH DRAW AMOUNT")
       userwithdraw=input("Would you like to withdraw?")
       if userwithdraw=="yes":
           account_id=(input("Enter account id"))
           amount=int(input("Emter amount you want to withdraw:"))
           cursor.execute (f'SELECT amount FROM Bank_Data.CreatingAcc WHERE account_id ={account_id}')
           current=0
           for num in cursor:
               for each in num:
                 each=current
                 if current < amount and amount<0:
                  print(f"Error: Insufficient amount for account_id {account_id}.")
                  return
                 else:
                  new_balance = current - amount
                  cursor.execute(f'UPDATE CreatingAcc SET amount = {new_balance} WHERE account_id ={account_id}')
                  print(f"Withdrew {amount} from account_id {account_id}. New balance is {new_balance}.")
           conn.commit()
withdraw_amount()
        
def check_balance():
        print("PRINT OUT THE BALANCE")
        cursor.reset()
        account_id=int(input("Enter account id:"))
        cursor.execute(f'SELECT amount FROM Bank_Data.CreatingAcc WHERE account_id ={account_id}')
        result_set = cursor.fetchall()
        if result_set:
            balance= result_set[0][0]
            print(f"amount for account_id {account_id}: {balance}")
        else:
            print(f"No account found with account_id {account_id}.")
            conn.commit()
check_balance()
def delete_data():
    print("DELETE ACCCOUNT")
    cursor.reset()
    account_id = int(input("Enter account id: "))
    cursor.execute(f"SELECT amount FROM Bank_Data.CreatingAcc WHERE account_id = {account_id}")
    result = cursor.fetchone()
    if result is None:
        print("Account not found.")
    else:
        cursor.execute(f"DELETE FROM Bank_Data.CreatingAcc WHERE account_id = {account_id}")
        conn.commit()
        print(f"Account {account_id} deleted.")
delete_data()          
                    