import numpy as np
arrn=[]
arrp=[]
totalp=0
def add(name,price):
    global totalp
    arrn.append(name)
    arrp.append(price)
    totalp=totalp+price
def view():
    print (arrn)
def main():
    while True:
        option=int(input("choose an option \n1.Add Items\n2.View Cart\n3.Total Price\n4.End"))
        if (option==1):
            name=input("Name of the item:")
            price=int(input("Price of the item"))
            add(name,price)
        elif option==2:
            view()
        elif option==3:
            print(totalp)
        elif option==4:
            break
main()
        
    
