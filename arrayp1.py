Arr=[]
for i in range(5):
    Arr.append(int(input(f"Enter {i} integer: ")))
summ=0
for i in range(5):
    summ=summ+Arr[i]
print("For loop sum: ",summ)    


print("Function sum: ",sum(Arr))

print(Arr)

