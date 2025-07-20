class Student:
    # Class variable
    school_name = "Green Valley High School"

    def __init__(self, name, roll_number, marks):
        # Instance variables
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(f"Student: {self.name}, Roll: {self.roll_number}, Marks: {self.marks}, School: {Student.school_name}")

student1 = Student("Amit", 101, 87)
student2 = Student("Neha", 102, 92)

student1.display()
student2.display()

Student.school_name = "Blue Ridge Academy"
student3 = Student("Amit", 101, 87)
student4 = Student("Neha", 102, 92)
student3.display()
student4.display()