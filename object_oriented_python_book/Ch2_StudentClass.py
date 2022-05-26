# Say we wanted to model a student in a course. 
# We could have a Student class that has instance variables:
#       for name, emailAddress, currentGrade, and so on. 
# 
# Each Student object we create from this class would have its own set of these instance variables, 
# and the values given to the instance variables would be different for each student.

class Student():
    def __init__(self, name, emailAddress, currentGrade):
        self.name = name
        self.emailAddress = emailAddress
        self.currentGrade = currentGrade

    def changeGrade(self, currentGrade):
        self.currentGrade = currentGrade

    def changeEmail(self, emailAddress):
        self.emailAddress = emailAddress

    def printStudent(self):
        print("\n Student's info:", self.name, self.currentGrade, self.emailAddress, '\n')

student1 = Student('Seba', 'name@email.com', '25')

student1.printStudent()
print(vars(student1))
print()