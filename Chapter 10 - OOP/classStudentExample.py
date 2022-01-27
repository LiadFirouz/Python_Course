import classPersonExample


class Student(classPersonExample.Person):

    def __init__(self, name='yoni', age=10, average_grades=70):
        super(Student, self).__init__(name, age)
        self.__average_grades = average_grades

    def set_average_grades(self, average_grades):
        self.__average_grades = average_grades

    def get_average_grades(self):
        return self.__average_grades

    def __str__(self):
        return "\nname: {}\nage: {} \naverage_grades: {}" \
            .format(Student.get_name(self), Student.get_age(self), Student.get_average_grades(self))
