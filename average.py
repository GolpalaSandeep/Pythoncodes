def get_numbers():    
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2st number:"))
    c=int(input("Enter 3rd number:"))
    d=int(input("Enter 4th number:"))
    return (a,b,c,d)
def cal(a,b,c,d):
    sum=(a+b+c+d)
    avg=sum/4
    return (sum,avg)
def display(sum,data):
    print(f"The sum is {sum} \n The average is {data}")

def main():
    (a,b,c,d)=get_numbers()
    sum,ans=cal(a,b,c,d)
    display(sum,ans)


main()