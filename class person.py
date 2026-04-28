class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old from {self.city}")


# Usage
p = Person("John", 25, "Cairo")
p.introduce()