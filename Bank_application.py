import Bank_functions
import mysql.connector
import random
##from newmain import account_exists

conn = mysql.connector.connect(user="root", database="Bank_Data", password="Hello1234")
cursor = conn.cursor()

account_id = 0

def user_selection():
    global account_id
    print("\nWelcome to Sejal Bank!")
    print(" _____________________")
    print("|1. Create account    |")
    print("|2. Login             |")
    print("|3. Delete Account    |")
    print("|4. Quit.             |")
    print("|_____________________|")
    
    user_choice = int(input("Would you like to create account or Login? (Enter 1, 2, 3 or 4) "))
    if user_choice == 1:
        create_account()
    elif user_choice == 2:
        login()  
    elif user_choice== 3:
        account_id = int(input("Enter account id: "))
        Bank_functions.delete_data(account_id) 
        user_selection()
    elif user_choice == 4:
        print("GoodBye!")
        quit()
    else:
        print("Invalid option")
        user_selection()
        
    conn.commit()
    while(True):
        print(" \n______________________")
        print("|1. Deposit            |")
        print("|2. Withdraw           |")
        print("|3. Check Balance      |")
        print("|4. Return to home page|")
        print("|______________________|")
        user_accountexists_choice = int(input("Would you like to Deposit, Withdraw or return: "))
        if user_accountexists_choice == 1:
            amount = int(input("Enter amount number:"))
            Bank_functions.deposit_amount(account_id, amount)
        elif(user_accountexists_choice == 2):
            amount = int(input("Enter amount you want to withdraw: "))
            Bank_functions.withdraw_amount(account_id, amount)
        elif(user_accountexists_choice==3):
            Bank_functions.check_balance(account_id)
        elif(user_accountexists_choice==4):
            user_selection()
        else:
            print("Invalid option")
            continue

def create_account():
    global account_id
    print("\n______________________")
    print("|1. Checking account  |")
    print("|2. Savings account   |")
    print("|3. Both              |")
    print("|4. Quit.             |")
    print("|_____________________|")
    acctype = input("Choose the series of numbers which will determine the account type: ")
    if acctype in ['1', '2', '3']:
        name = input("Enter name: ")
        dob = input("Enter DOB (YYYY-MM-DD): ")
        account_id_str = ''.join([str(random.randint(0, 9)) for i in range(7)])
        account_id = int(account_id_str)
        print("Account name: " + name)
        print("Account type: " + acctype)
        print("Date of birth: " + dob)
        print("Account ID: " + account_id_str)
        Bank_functions.create_account(name, acctype, dob, account_id)
        pinnum = int(input("Enter pin number(4 Digit): "))
        pinnum2 = int(input("Enter pin again: "))
        while(pinnum!= pinnum2):
            pinnum2 = int(input("PIN does not match, try again"))
    elif acctype == 4:
        print("GoodBye!")
        quit()
    else:
        print("Invalid account type")
        create_account()



def login():
    global account_id
    account_id = int(input("Enter account Id"))
    if Bank_functions.account_exists(account_id):
        print("Login successful")
    else:
        again = input("Cannot login! Try again? (Yes/No): ")
        if again == "Yes":
            login()
        else:
            quit()
user_selection()
