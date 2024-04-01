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




# Since now everything related to students is in the Student class, 
# now we can do a lot more with the data validation / stadardization
# like check if name is not empty or house is a valid house.

# This is the capability of OOP which you will not get in Dictionary
# i.e. if you add a key to a dict, it's going in no matter what
# even if the name is empty or the house is invalid, it is going to that dict.
# But with class (and by way of this init method), we can control that.
# So we have more control now over the correctness.
  
class Student:
  def __init__(self, name, house):
    if not name:
      raise ValueError("Missing Name")
    self.name = name

    if house not in ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']:
      raise ValueError("Invalid House")
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
'''


# If we look at the main function we are still printing student's name and house manually
# We are going in the student object and accessing name and house
# How about just printing stundent altogether: print(student)
# So we use __str__ which is another special method, 
# if you define inside of your class, Python will automatically call this funtion
# anytime some other function like print wants to see your object as a string.
  
class Student:
  def __init__(self, name, house):
    if not name:
      raise ValueError("Missing Name")
    self.name = name

    if house not in ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']:
      raise ValueError("Invalid House")
    self.house = house


  def __str__(self):
    return f"{self.name} from {self.house}"
  

def main():
  student = get_student()
  print(student)


def get_student():
  name = input("Name: ")
  house = input("House: ")
  return Student(name, house)

if __name__ == "__main__":
  main()
  
