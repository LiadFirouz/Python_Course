import classPersonExample


class Teacher(classPersonExample.Person):

    def __init__(self, name, age, salary):
        # classPersonExample.Person.__init__(self, name, age)
        super(Teacher, self).__init__(name, age)
        self.__salary = salary

    def say(self):
        print("Good morning students!")
