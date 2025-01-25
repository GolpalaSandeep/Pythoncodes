def passcheck(string):
    lower=False
    upper=False
    Symbols=False
    digits=False
    if(len(string)<8):
        return False
    for char in string:
        if(char.islower()):
            lower=True
        elif(char.isupper()):
            upper=True
        elif(char.isdigit()):
            digits=True
        else:
            Symbols=True
    if(lower and upper and Symbols and digits):
        return True
    else:
        return False
string=input("Enter the password")
if(passcheck(string)):
    print("Strong Password")
else:
    print("Weak password")
    