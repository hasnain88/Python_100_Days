class Student:
    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        
    def display(self):
        return f"Student Name: {self.name}, Roll No: {self.roll_number}, Marks: {self.marks}"
    
student1 = Student("Amit",101,87.5)
student2 = Student("Neha",102,91.0)
student3 = Student("Ravi",103,76.5)

print(student1.display())
print(student2.display())
print(student3.display())