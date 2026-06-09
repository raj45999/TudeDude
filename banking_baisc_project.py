'''

THIS IS A BASIC PROJECT DISPLAYING SOME BASIC WORKING OF BANKING SYSTEMS...
IT HAVE 5 FUNCTIONS IN TOTAL FROM CHECKING, DEPOSIT, WITHDRAWL OF CASH AND CHECKING,SUBMITTING OF DOCUMENTS...

'''







print("========================")
print("Welcome to ABC Bank!!!")# Tittle in starting...
print("========================")
print()
Balance = 0.0
updated_kyc={}
def check_balance():# function for checking balance 
    print("========================")
    print(f"Your current Balance is {Balance}")
    print("========================")


def deposit(Amount):# function for depositing money
    global Balance
    print("========================")
    if Amount > 0:
        print(f"{Amount} Deposited Sucessfully!!!")
        Balance = Balance + Amount
        print("Amount deposited Successfully!!")
        print("========================")
    else:
        print("Amount Invalid for deposting!!\n Please enter a correct amount and try again...")
        print("========================")


def withdrawl(Amount):#function for withdrawl of money
    global Balance
    print("========================")
    if Amount > Balance:
        print("Insufficient Balnce!!\n Please try again...")# if money for withdrawl is higher than bank balance
        print("========================")
    elif Amount > 0 and Amount<= Balance:
        print(f"{Amount} Withdrawn Sucessfully!!!")
        Balance -= Amount 
        print("Amount withdrawn Successfully!!")
        print("========================")
    else:
        print("Amount Invalid for Withdrawl!!\n Please enter a correct amount and try again...")#if something else is entered instead of amount
        print("========================")

def update_kyc(**docs):#for entering documents
    updated_kyc.update(docs)
 
    print()
    print("========================")
    print("Your document is saved successfully!!")
    print("========================")
    print()

def check_kyc():#for checking submitted documents
    global updated_kyc
    if len(updated_kyc)== 0:#if no document is submitted
        print()
        print("========================")
        print("No document Found!!\nPlease submit your documents first...")
        print("========================")
        print()
    else:
        for key in (updated_kyc):#displaying the submitted document
            print()
            print("========================")
            print(f"{key} : {updated_kyc[key]}")
            print("========================")
            print()



if __name__ == "__main__":#condtion so that this can be aslo used as module in any other project
    while True:#infinnite function
        
        print("Please Enter the S.no of Service you want to use...")# Knowledge about services
        print("========================")
        print("1.Check Balance")
        print("2.Dposit Money")
        print("3.Withdrawl Money")
        print("4.Submit Documents")
        print("5.Check Submitted Documnets")
        print("6.Exit") 
        print("========================")
        print()
        choice= input("Enter the service number; ")#input from user
        if choice=='1': # Services choice given here
            print("Checking....")
            print()
            check_balance()
            print()
        elif choice=='2':
            Amt=float(input("Please Enter the Amount; "))#changing into float for checking balances...
            print()
            deposit(Amt)
            print()
        elif choice=='3':
            Amt=float(input("Please Enter the Amount; "))#changing into float for checking balances...
            print()
            withdrawl(Amt)
            print()
        elif choice=='4':
            no_of_documents=int(input("Enter the number of Documents: "))
            for i in range(no_of_documents):
                name = input("Enter the name of Document: ")
                id = input("Enter the ID of document: ")
                update_kyc(name=id)
        elif choice=='5':
            check_kyc()
        elif choice=='6':
            print()
            print("========================")
            print("Thank You for Banking with us\n Have a nice day...")# Exit line
            print("========================")
            print()
            break
            
        else:
            print()
            print("========================")
            print(" Invalid number!!\nPlease Enter a Correct Number") # if someone input anything wrong...
            print("========================")
            print()
