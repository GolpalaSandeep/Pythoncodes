def billsplit(total,num,tip):
    return int((total+(tip/100)*total)/num)
total=int(input("Enter total amount"))
num=int(input("Enter total number of people"))
tip=float(input("Enter tip percentage"))
print ("Each person has to pay:",billsplit(total,num,tip))
