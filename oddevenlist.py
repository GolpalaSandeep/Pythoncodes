import numpy as np
arr=[]
odd=[]
even=[]
def oddeven(arr):
    for num in arr:
        if(num%2==0):
            even.append(num)
        else:
            odd.append(num)
    print ("Even : ",even)
    print ("Odd : ",odd)
n=int(input("Enter the number of numbers: "))
print(f"Enter {n} numbers: ")
for i in range(n):
    arr.append(int(input()))
oddeven(arr)
