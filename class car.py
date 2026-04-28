class Car:
    def __init__(self, brand, model, year, color="white"):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0  # always starts at 0

    def get_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Color: {self.color}, Speed: {self.speed}")


# Usage
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("BMW", "M3", 2023, "black")

car1.get_info()  # color will be white
car2.get_info()  # color will be black