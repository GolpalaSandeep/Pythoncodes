def checkpalin(string):
    rstring=string[::-1]
    if string==rstring:
        return True
    else:
        return False
string=input("Enter the string: ")
if(checkpalin(string)):
    print("Yes")
else:
    print("No")