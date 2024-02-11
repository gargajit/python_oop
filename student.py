def main():
    #name, house = get_student()        # no need to unpack if you are using a tuple explicitly 
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #return name, house          # this is not returning 2 values rather it is returning one value in form of tuple
    #explicitly
    return (name, house)

if __name__ == "__main__":
    main()
