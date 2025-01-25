def seclargest(arr):
    max=-float('inf')
    secmax=-float('inf')
    for i in arr:
        if(i>max):
            secmax=max
            max=i
        elif (i>secmax and i!=max):
            secmax=i
    return secmax
arr=[]
n=int(input("Enter the number of numbers: "))
for i in range(n):
    arr.append(int(input()))
print("second largest is: ",seclargest(arr))
