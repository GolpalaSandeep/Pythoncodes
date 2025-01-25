def checkleap(num):
    return num%4==0
while True:
    num=int(input("Enter the year: "))
    if(checkleap(num)):
        print("Leap year")
    else:
        print("Not a leap year")
    
