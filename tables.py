def table(num,s,e):
    for i in range(s,e+1):
        print(f"{num} x {i} = ",num*i)
num=int(input("Enter the number: "))
start=int(input("Enter the starting range: "))
end=int(input("Enter the ending range: "))
table(num,start,end)