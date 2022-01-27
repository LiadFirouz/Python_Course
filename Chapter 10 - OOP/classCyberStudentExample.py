import classStudentExample


class CyberStudent(classStudentExample.Student):
    def __init__(self, name, age, grade, cyber_grade):
        super(CyberStudent, self).__init__(name, age, grade)
        self.__cyber_grade = cyber_grade

    def get_cyber_grade(self):
        return self.__cyber_grade
