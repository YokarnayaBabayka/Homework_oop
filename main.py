print('Hello, World!')


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lc_grades:
                lecturer.lc_grades[course] += [grade]
            else:
                lecturer.lc_grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if len(self.grades) > 0:
            sum_ = 0
            count = 0
            for v in self.grades.values():
                for i in v:
                    sum_ += i
                    count += 1
            return sum_ / count
        else:
            return 0

    def __str__(self):
        res = f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.average_grade()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}
'''
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lc_grades = {}

    def average_lc_grade(self):
        if len(self.lc_grades) > 0:
            sum_ = 0
            count = 0
            for v in self.lc_grades.values():
                for i in v:
                    sum_ += i
                    count += 1
            return sum_ / count
        else:
            return 0

    def __str__(self):
        res = f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.average_lc_grade()}
'''
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_lc_grade() < other.average_lc_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


# Создаем студентов
best_student = Student('Vasya', 'Pupkin', 'm')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Основы основ']

next_student = Student('Masha', 'And-bear', 'f')
next_student.courses_in_progress += ['Python', 'Git']
next_student.finished_courses += ['Основы основ']

# Создаем лекторов
lecturer_1 = Lecturer('Karl', 'Son')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Fun', 'Tic')
lecturer_2.courses_attached += ['Git']

# Создаем проверяющих
reviewer_1 = Reviewer('Loch', 'Ness')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Los', 'Alamos')
reviewer_2.courses_attached += ['Git']

# Проверяющий оценивает студента
reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(next_student, 'Python', 2)

reviewer_2.rate_hw(best_student, 'Git', 10)
reviewer_2.rate_hw(next_student, 'Git', 4)

# Студент оценивает лектора
best_student.rate_lc(lecturer_1, 'Python', 10)
next_student.rate_lc(lecturer_1, 'Python', 8)

best_student.rate_lc(lecturer_2, 'Git', 9)
next_student.rate_lc(lecturer_2, 'Git', 7)

print(best_student)
print(next_student)
print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)
print(best_student > next_student)
print(lecturer_1 < lecturer_2)

# Задача 4

all_students = [best_student, next_student]
all_lecturers = [lecturer_1, lecturer_2]

# print(best_student.grades)
# print(next_student.grades)
#
# print(lecturer_1.lc_grades)
# print(lecturer_2.lc_grades)

def avg_grade_in_course(students, course):
    all_grades_in_course = []
    for student in students:
        if course in student.grades:
            for _ in student.grades[course]:
                all_grades_in_course.append(_)
                # print(all_grades_in_course)
    avg_grade_in_course = round(sum(all_grades_in_course) / len(all_grades_in_course), 1)
    return avg_grade_in_course

print(avg_grade_in_course(all_students, 'Python'))

def avg_lc_grade_in_course(lecturers, course):
    all_lc_grades_in_course = []
    for lecturer in lecturers:
        if course in lecturer.lc_grades:
            for _ in lecturer.lc_grades[course]:
                all_lc_grades_in_course.append(_)
                # print(all_lc_grades_in_course)
    avg_lc_grade_in_course = round(sum(all_lc_grades_in_course) / len(all_lc_grades_in_course), 1)
    return avg_lc_grade_in_course

print(avg_lc_grade_in_course(all_lecturers, 'Python'))