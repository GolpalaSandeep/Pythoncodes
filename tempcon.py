def CtoF():
    temp=float(input("Enter the temperature in Celsius: "))
    ans=float(((9/5)*(temp)+32))
    print(ans)
def FtoC():
    temp=float(input("Enter the temperature in Fahrenheit: "))
    ans=float((5/9)*(temp-32))
    print(ans)
def KtoF():
    temp=float(input("Enter the temperature in Kelvin: "))
    ans=(temp-273.15)*(9/5)+32

    print(ans)
def KtoC():
    temp=float(input("Enter the temperature in Kelvin: "))
    ans=temp-273.15
    print(ans)
def FtoK():
    temp=float(input("Enter the temperature in Fahreinhiet: "))
    ans=(((temp-32)*5)/9)+273.15
    print(ans)
    
def CtoK():
    temp=float(input("Enter the temperature in Celsius: "))
    ans=temp+273.15

    print(ans)

def main():
    while True:
        option=int(input("choose the conversion type 1.Celsius to Fahreinheit\n2.Fahreinheit to Celsius\n3.Kelvin to Fahreinheit\n4.Kelvin to Celsius\n5.Fahreinheit to kelvin\n6.Celsius to Kelvin\n7.End"))
        if(option==1):
            CtoF()
        elif(option==2):
            FtoC()
        elif(option==3):
            KtoF()
        elif(option==4):
            KtoC()
        elif(option==5):
            FtoK()
        elif(option==6):
            CtoK()
        elif(option==7):
            break

main()

