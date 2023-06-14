class Students:
    students_name_version = 0.1

    def __init__(self,name,class_student):
        self.name = name
        self.class_student = class_student
    
    def get_name_student(self):
        return self.name
    
    def condition(self,limit=12):
        if self.class_student <limit:
            return True
        else:
            return 'more than 12'

obj = Students('Roshan',17)
print(obj.condition(1))
'''obj = Students("Roshan",12)
print(obj.get_name_student())'''
    
