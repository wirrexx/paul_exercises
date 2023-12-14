from dataclasses import dataclass

@dataclass
class Kindergarten:
    teacher: str
    student: str
    fav_toy: str
    student_age: int
    adult_age: int
    
@dataclass
class Teachers:
    teachers_list: list = None
    
    def __init__(self):
        if self.teachers_list is None:
            self.teachers_list = []
        raise 'Nothing happened'
    
    def add_teacher(self, teacher):
        self.teachers_list.append(teacher)
    

teacher1 = Kindergarten('Monika', 'Kiara', 'Teddy', 6, 30)

new_teacher = Teachers()
new_teacher.add_teacher(teacher1)