class Student():
    def __init__(self,name,class_student):
        self.__name = name
        self.class_student = class_student 

class Teacher(Student):
    def __init__(self,name,class_student,teacher_name,teacher_id):
        Student.__name = name
        Student.class_student = class_student
        
        self.teacher = teacher_name
        self.teacher_id = teacher_id

record = Teacher('Roshan', 12, 'Aashita', 117563475)
print(record.__dict__)

record2 = Student('Roshan',12)
print(record2._Student__name)