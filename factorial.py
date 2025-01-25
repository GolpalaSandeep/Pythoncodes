def factorial(num):
    ans=1
    if(num==0):
        return 1
    if(num==1):
        return 1
    for i in range(num,1,-1):
        ans=ans*i
    return ans
num=int(input("Enter the number: "))
print(factorial(num))
