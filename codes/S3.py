class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(
            f"Привет! Меня зовут {self.name}. Мне {self.age}.")
class Student(Person):
    def __init__(self,name,age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} учится на {self.course} курсе.")

# Создание "объкетов"
person1 = Person('Вадим', 25)
person1.greet()
print("")

student1 = Student("Афина", 20, 3)
student1.greet()
student1.study()
