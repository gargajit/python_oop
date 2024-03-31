'''
class Student:
  ...            

# that's enough code, lines 2&3 to just invent a new data type Student
# that may or may not have some future functionlity as well.

def main():
  student = get_student()
  print(f"{student.name} from {student.house}")

def get_student():
  student = Student()    # Here we are creating an object* of the class Student
  student.name = input("Name: ")    #student.name is an attribute to the student variable
  student.house = input("House: ")  #student.house is another attribute to the student variable
  return student

if __name__ == "__main__":
  main()



So we create **`objects from classes.`** 

If `class` is a blueprint/mold then an `object` is when you use that blueprint to something specific.
'''

class Student:
  def __init__(self, name, house):
    self.name = name
    self.house = house

def main():
  student = get_student()
  print(f"{student.name} from {student.house}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  return Student(name, house)  # returning the return value of this Student() function that is constructing my new object

if __name__ == "__main__":
  main()
