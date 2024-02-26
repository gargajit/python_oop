class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
# Everything related to the student is in the class Student. 
# The only other things in the file are the main and the conditional.

def main():
  student = Student.get()
  print(student)



if __name__ == "__main__":
  main()
