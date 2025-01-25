import random
def randomm():
    num=random.randrange(1,100)
    return num
def main():
    num=randomm()
    print(num)
    while True:
        ans=int(input("Guess the number"))
        if(ans>num):
            print("High")
            continue
        elif(ans<num):
            print("Low")
            continue
        elif(ans==num):
            print("Correct answer")
            break
main()


