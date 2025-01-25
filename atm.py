balance=0
def checkbalance():
    print(f"{balance} Rupees")
def deposit(money):
    global balance
    balance=balance+money
def withdraw(money):
    global balance
    if(money>balance):
        print("Insufficient balance for withdrawl")
    balance=balance-money
def main():
    while True:
        print("Choose the option 1.Check Balance 2.Deposit 3.Withdraw 4.End")

        option=int(input())
        if (option==1):
            checkbalance()
        if(option==2):
            money=int(input("Enter money to deposit: "))
            deposit(money)
        if(option==3):
            money=int(input("Enter money to withdraw: "))
            withdraw(money)
        if(option==4):
            break

main()

              




