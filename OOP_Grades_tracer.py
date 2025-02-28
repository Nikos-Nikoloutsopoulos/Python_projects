import os

class Student():
    def __init__(self, name):
        self.name=name
        self.grades ={"Math":0, "Science":0,"History":0}
    
    def __str__(self):
        return (f"Student is {self.name} with grades {self.grades["Math"]},{self.grades["Science"]},{self.grades["History"]}")
    
    def update_grade(self, subject, grade):
        self.grades[subject]  =grade
    

class Gradebook():
    def __init__(self):
        self.students= {}

    def __str__(self):
        output ="Current student:\n"
        for name, student in self.students.items():
            output +=str(student) +"\n"
        return output
    
    def add_student(self,name):
        student =Student(name)
        self.students[name] = student
    
    def remove_student(self,name):
        if name in self.students:
            del self.students[name]
            return True
        return False

    def update_grade(self, name, subject, grade):
        if name in self.students:
            student= self.students[name]
            student.update_grade(subject,grade)
            return True
        return False

gradebook =Gradebook()

choice=True
while choice is True:
    try:
        print(" 1 Add a student")
        print(" 2 Update a student grade")
        print(" 3 Remove a student")
        print(" 4 Show all students")
        print(" 5 Quit")

        item= int(input("Choise one of the following actions:"))


        os.system('cls')
        if item==1:
            student_name=str(input("Enter student name:"))
            student1=Student(student_name)
            print(student1)

            gradebook.add_student(student_name)
        elif item ==2:
            student_name=input("Enter student name:")
            subject=input("Enter subject name:")
            grade=int(input("Enter subject grade:")) 
            if gradebook.update_grade(student_name,subject,grade):
                print(f"{student_name}'s grade in {subject} s now {grade}")
            else:
                print (f"{student_name} not found in the list")
        elif item ==3:
            student_name=str(input("Enter student name:"))
            if gradebook.remove_student(student_name):
                print(f"You remove {student_name} from the list")  
            else:
                print(f"{student_name} not found in the list") 
        elif item ==4:
            print(gradebook)
        elif item ==5:
            print("Quit")
            choice=False
        else:
            print("Enter a correct number and try again")

    except ValueError or NameError:
        print("Incorrect choise")          