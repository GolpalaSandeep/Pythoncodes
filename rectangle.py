def display(data):
    print(f"The area is {data}")

def get_input():
    r_length=input("Length:")
    r_width=input("Width:")

    return(r_length,r_width)

def c_area(length,width):
    area=int(length)*int(width)
    return area

def main():
    (length,width)=get_input()

    area=c_area(length,width)
    display(area)


main()

