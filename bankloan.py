count=0
def checkelgblty(sal,age,creditscore):
    if(sal>30000):
        pass
    else:
        print("Ineligible,salary is low")
        return
    if(age>25):
        pass
    else:
        print("Ineligible,age is low")
        return
    if(creditscore>=750):
        pass
    else:
        print("Ineligible,credit score is low")
        return
    print ("Eligible")
    return
def main():
    sal=int(input("Enter Salary: "))
    age=int(input("Enter age: "))
    creditscore=int(input("Enter cs: "))
    checkelgblty(sal,age,creditscore)
main()


