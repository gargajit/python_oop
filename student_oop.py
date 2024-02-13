class Student:
  ...            

# that's enough code, lines 1&2 to just invent a new data type Student
# that may or may not have some future functionlity as well.

def main():
  student = get_student()
  print(f"{student.name} from {student.house}")

def get_student():
  student = Student()    # Here we are creating an object* of the class Student
  student.name = input("Name: ")
  student.house = input("House: ")
  return student

if __name__ == "__main__":
  main()


'''
So we create **`objects from classes.`** 

If `class` is a blueprint/mold then an `object` is when you use that blueprint to something specific.
'''
