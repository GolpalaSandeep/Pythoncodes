def studentgrade(name,s1,s2,s3,s4,s5):
    totalmarks=s1+s2+s3+s4+s5
    percentage=(totalmarks/500)*100
    if(percentage>=85): grade="A"
    elif(percentage>=75 and percentage<85): grade="B"
    elif(percentage>=60 and percentage<75): grade="C"
    elif(percentage>=45 and percentage<60): grade="D"
    elif(percentage<45): grade="Fail"
    print (totalmarks,percentage,grade)
def main():
    name=input("Enter name of the student")
    s1=int(input("Enter marks in s1 "))
    s2=int(input("Enter marks in s2 "))
    s3=int(input("Enter marks in s3 "))
    s4=int(input("Enter marks in s4 "))
    s5=int(input("Enter marks in s5 "))

    studentgrade(name,s1,s2,s3,s4,s5)
main()

    