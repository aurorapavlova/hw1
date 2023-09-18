class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_rate(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 2)
        return res

    def avg_rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.avg_rate()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Разные категории людей.")
            return
        return self.avg_rate() < other.avg_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_rate(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 2)
        return res

    def avg_rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rate()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Разные категории людей.")
            return
        return self.avg_rate() < other.avg_rate()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


student_1 = Student('Aurora', 'Pavlova', 'female')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Ivan', 'Ivanov', 'male')
student_2.courses_in_progress += ['Python', 'C+']
student_2.finished_courses += ['Java']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python', 'C+', 'Java']

reviewer_2 = Reviewer('John', 'Whyte')
reviewer_2.courses_attached += ['Python', 'VC']

lecturer_1 = Lecturer('Stepan', 'Sidorov')
lecturer_2 = Lecturer('Marat', 'Utyashev')

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 10)

student_1.rate_lect(lecturer_1, 'Python', 4)
student_1.rate_lect(lecturer_2, 'Python', 6)
student_2.rate_lect(lecturer_1, 'Python', 6)
student_2.rate_lect(lecturer_2, 'Python', 5)

student_list = [student_1, student_2]
lector_list = [lecturer_1, lecturer_2]

print(student_1)
print(student_2)
print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)

print(student_1 < student_2)
print(lecturer_1 > lecturer_2)
print(student_1 < lecturer_1)


def avg_rate_course_std(course, student_list):
    sum_ = 0
    qty_ = 0
    for std in student_list:
        for crs in std.grades:
            std_sum_rate = std.avg_rate_course(course)
            sum_ += std_sum_rate
            qty_ += 1
    res = round(sum_ / qty_, 2)
    return res


def avg_rate_course_lct(course, lector_list):
    sum_ = 0
    qty_ = 0
    for lct in lector_list:
        for crs in lct.grades:
            lct_sum_rate = lct.avg_rate_course(course)
            sum_ += lct_sum_rate
            qty_ += 1
    res = round(sum_ / qty_, 2)
    return res


print(avg_rate_course_std('Python', student_list))

print(avg_rate_course_lct('Python', lector_list))
