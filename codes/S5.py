class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Имя: {self.name}\nВозраст: {self.age}\n")


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def show_info(self):
        print(f"Имя: {self.name}\nВозраст: {self.age}\nКурс: {self.course}\n")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_info(self):
        print(f"Имя: {self.name}\nВозраст: {self.age}\nПредмет: {self.subject}\n")

person1 = Person("Афина", 22)
person1.show_info()

student1 = Student("Вадим", 25, 2)
student1.show_info()

teacher1 = Teacher("Иванов Иван", 45, "Программная инженерия")
teacher1.show_info()
