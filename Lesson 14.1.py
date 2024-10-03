class GroupLimitError(Exception):

    def __init__(self, message="Неможливо додати більше 10 студентів у групу"):
        self.message = message
        super().__init__(self.message)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Human {self.first_name}, {self.last_name}, Gender: {self.gender}, Age: {self.age}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student: {self.first_name}, {self.last_name}, Gender: {self.gender}, Age: {self.age}, Record book: {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Vasya', 'idk', 'AN142')
st2 = Student('Female', 25, 'Katya', 'idk', 'AN145')
st3 = Student('Male', 22, 'Artem', 'idk', 'AN146')
st4 = Student('Female', 23, 'Vika', 'idk', 'AN147')
st5 = Student('Male', 24, 'Misha', 'idk', 'AN148')
st6 = Student('Female', 26, 'Sofa', 'idk', 'AN149')
st7 = Student('Male', 27, 'Oleg', 'idk', 'AN150')
st8 = Student('Female', 28, 'Masha', 'idk', 'AN151')
st9 = Student('Male', 29, 'Sasha', 'idk', 'AN152')
st10 = Student('Female', 21, 'Anna', 'idk', 'AN153')
st11 = Student('Male', 20, 'Mark', 'idk', 'AN154')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

try:
    gr.add_student(st11)
except GroupLimitError as e:
    print(f"Помилка: {e}")

print(gr)
