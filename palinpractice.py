def ispalin(str):
    nstr=""
    prev_char=str[0]
    for charf in str:
        if(prev_char==" " and charf==" "):
            nstr+=" "
        else:
            nstr+=charf
        prev_char=charf
    print (nstr)
            
    list1=nstr.split(" ")
    print(list1)
    for word in list1:
        trueorfalse=True
        for i in range(int(len(word)/2)):
            if(word[i]!=word[len(word)-i-1]):
                trueorfalse=False
                break
        if trueorfalse:
            return word
        
    return "No palindrome"
    
def main():
    while True:
        str=input("Enter the string: ")
        ans=ispalin(str)
        print(ans)
main()
                
