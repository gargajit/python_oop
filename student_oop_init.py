class Student:
  def __init__(self, name, house):
    if not name:      # ie Pythonic way to say -> if name == ""
      raise ValueError("Missing Name")
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid House")
    self.name = name
    self.house = house

'''
The __init__ function inside the class Student will always be called when the Student function is invoked.
This is the way to implement the initialization of an object in Python.
'''

def main():
  student = get_student()
  print(f"{student.name} from {student.house}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  return Student(name, house)


if __name__ == "__main__":
  main()


'''
How to store the values of the instance variables (here, name and house) in the current object that has just been instantiated? 
(that was just created at the time of the Constructor Call) Student(name, house)

Python authors decided that the __init__ method, along with the other arguments takes one other argument 
(by convention, it's called self), that has to come first. 
And self, as its name implies, gives you access to the current object that was just created. 
def __init__(self, name, house):

It means at the Constructor level, it constructs an object in the Computer's memory. 
Then, Python automatically calls the __init__ method, 
and it's going to automatically pass in a reference to an argument that represents the current object 
that it just constructed in memory for you, now available to populate it with values.
self.name = name
self.house = house

self.name and self.house creates new instance variables and puts the passed name and house inside of it respectively.
This is like installing into the otherwise empty object the value name and house and storing them in, 
identically named instance variables (respectively) in the object.
And again, an object is just an instance of a class.
'''
