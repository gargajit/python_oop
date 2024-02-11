#Tuple is similar to list in spirit but it is **immutable**. Hence the values cannot be modified.
# If tried to modify, it will throw TypeError: 'tuple' object does not support item assignment

def main():
    #name, house = get_student()        # no need to unpack if you are using a tuple explicitly 
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #return name, house          # This is not returning 2 values rather it is returning one value in the form of a tuple
    #explicitly
    return (name, house)

if __name__ == "__main__":
    main()
