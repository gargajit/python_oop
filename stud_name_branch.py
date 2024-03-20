'''
We have a class defined for Student. Create two new object for students called stud1 and stud2. 
Set stud1 name as ‘Robin’ and branch ‘CSE’ and stud2 name as ‘Rahul’ and branch as ‘ECE’.
'''

class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
    def printfunction(self):
        print(self.name + " " + self.branch)

def main():
    #Your code goes here
    stud1 = Student("Robin", "CSE")
    stud2 = Student("Rahul", "ECE")
    
    stud1.printfunction()
    stud2.printfunction()
    return 0

if __name__ == '__main__':
    main()
