def pattern(num):
    for i in range(0,num):
        for j in range(0,i+1):
            print("*",end="")
        print("")
def rpattern(num):
    for i in range(num,0,-1):
        for j in range(i,0,-1):
            print("*",end="")
        print("")
num=int(input("Enter a number: "))
pattern(num)
rpattern(num)

