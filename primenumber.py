import math
def isprime(n):
        
        if (n==2):
             return True
        if(n%2==0) or n<2:
            return False
        
        for i in range(3,int(math.sqrt(n))+1,2):
                    
                    if(n%i==0):
                        return False
        return True         
                    
  
def main():
    while(True):
          n1=int(input("Enter starting number : "))
          n2=int(input("Enter ending number : "))
          if(n1>0 and n2>0 and n1<n2):
                break
          print("Enter valid numbers")
    c=0
    for n in range(n1,n2+1):
         v=isprime(n)
         if(v):
              print(n)
        

main()