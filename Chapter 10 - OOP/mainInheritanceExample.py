import classStudentExample
import classTeacherExample


def main():
    teacher1 = classTeacherExample.Teacher("Barak", 40, 100)
    print(teacher1)
    student1 = classStudentExample.Student()
    print(student1)
    print(student1.get_average_grades())
    student1.set_average_grades(50)
    print(student1.get_average_grades())
    student2 = classStudentExample.Student("ofir", 14, 50)
    print(student2.__str__())
    teacher1.say()

if __name__ == '__main__':
    main()
