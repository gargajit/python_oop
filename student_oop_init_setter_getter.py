class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:              # ie Pythonic way to say -> if name == ""
            raise ValueError("Missing Name")
        self._name = name
        
    @property
    def house(self):
       return self._house
    
    @house.setter
    def house(self, house):
       if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
       self._house = house
    

def main():
  student = get_student()
  #student.house = "Number 4"
  print(student)


def get_student():
  name = input("Name: ")
  house = input("House: ")
  return Student(name, house)


if __name__ == "__main__":
  main()
