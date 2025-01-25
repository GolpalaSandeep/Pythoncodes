vowels=0
consonants=0
digits=0
symbols=0
vow="aeiouAEIOU"
con="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
dig="1234567890"
def stringanlys(string):
    vowels=0
    consonants=0
    digits=0
    symbols=0
    for i in range(0,len(string)):
        char=string[i]
        if(char in vow ):
            vowels=vowels+1
        elif(char in con ):
            consonants=consonants+1
        elif(char in dig):
            digits=digits+1
        elif(char==' '):
             pass
        else:
            symbols=symbols+1
    print ("vowels:",vowels,"Consonants",consonants,"digits:",digits,"Symbols:",symbols)
string=input("Enter the string:")
stringanlys(string)
