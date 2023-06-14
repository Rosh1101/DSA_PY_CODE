class Students:
    students_name_version = 0.1

    def __init__(self,name,class_student):
        self.name = name
        self.clas_student = class_student
    
'''student_object = Students('Roshan',17)
print(student_object.__dict__)
print(student_object.name)
delattr(student_object,"name")'''
object_attr = Students('Roshan',12)
#object_attr.students_name_version
print(object_attr.students_name_version)