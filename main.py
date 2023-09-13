class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        for i in self.grades.values():
            self.average_grade = sum(i) / len(i)
            res = (f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}")
            return res

    def average_grade_on_the_course(persons, course):
        if not isinstance(persons, list):
            return "Not list"
        all_average_grade = []
        for person in persons:
            all_average_grade.extend(person.average_grade_course.get(course, []))
        if not all_average_grade:
            return "По такому курсу ни у кого нет оценок"
        return round(sum(all_average_grade) / len(all_average_grade), 2)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        del Mentor.rate_hw

    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))}"
        return res

    def __lt__(self, student):
        if not isinstance(student, Student):
            print('Not a Student!')
            return
        return sum(sum(self.grades.values(), [])) < sum(sum(student.grades.values(), []))


class Reviewer(Mentor):
    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname}"
        return res


#Students
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

good_student = Student('Aurora', 'Pavlova', 'female')
good_student.courses_in_progress += ['Python']
good_student.courses_in_progress += ['Git']
good_student.finished_courses += ['Введение в программирование']

# --
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']


cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 10)

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'Git', 10)

cool_reviewer = Reviewer('Some', 'Buddy')
good_reviewer = Reviewer('John', 'Whyte')

print(best_student)
print(best_student.grades)
print(cool_reviewer)
print(cool_lecturer)
print(cool_lecturer.__lt__(best_student))
