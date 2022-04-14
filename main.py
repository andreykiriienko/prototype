import copy


class Students:
    def __init__(self, number_of_students, exam, passed_the_exam):
        self.number_of_students = number_of_students
        self.exam = exam
        self.passed_the_exam = passed_the_exam

    def __str__(self):
        return f'{self.number_of_students}: Екзамен по {self.exam}: Сдало еказмен {self.passed_the_exam} учеников'


class Person:
    def __init__(self, name_class, students):
        self.name_class = name_class
        self.students = students

    def __str__(self):
        return f'Класс: {self.name_class} : Колличество учеников: {self.students}'


classA = Person('A', Students(30, 'Матеманике', 25))

classB = copy.deepcopy(classA)
classB.name_class = 'B'
classB.students.number_of_students = 26
classB.students.passed_the_exam = 20

print(f'{classA}\n{classB}')
