import dis
def getandcompare():
    a=int(input("Enter 1st number "))
    b=int(input("Enter 2nd number "))

    if(a>b): 
        max1=a
        s1="a"
    else: 
        max1=b
        s1="b"

    c=int(input("Enter 3rd number "))
    d=int(input("Enter 4th number "))

    if(c>d): 
        max2=c
        s2="c"

    else: 
        max2=d
        s2="d"
    if(max1>max2): return max1,s1
    else: return max2,s2
def greatest(a,b,c):
     if(a>b):
         if (a>c):
             return "a",a
     else:
         if(b>c):
             return "b",b
         else:
             return "c",c

def display(ans,s):
    print(f"the greatest number is {s}={ans}")
    
def main():
    ans,s=getandcompare()
    display(ans,s)
    dis.dis(getandcompare)
    
main()


