# =========================================================================================
# Using Tuple
# ==========================================================================================

'''
# Tuple is similar to list in spirit but it is **immutable**. Hence the values cannot be modified.
# If tried to modify, it will throw TypeError: 'tuple' object does not support item assignment

def main():
    #name, house = get_student()        # no need to unpack if you are using a tuple explicitly 
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #return name, house      # This is not returning 2 values rather it is returning one value in the form of a tuple
    #explicitly
    #return (name, house)



# So just in case, if by design you want to accept mutability and allow changes,
# Instead of returning a (tuple) you can return a [list] 
    
    #return [name, house]
    

if __name__ == "__main__":
    main()
'''


# ===============================================================================
# Using Dictionary
# ===============================================================================
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

'''
def get_student():
    student = {}
    student['name'] = input("Name: ")
    student['house'] = input("House: ")
    return student
'''
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {'name': name, 'house': house}


if __name__ == "__main__":
    main()
