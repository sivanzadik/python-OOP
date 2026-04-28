class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def describe(self):
        print(f"Rectangle: {self.width} x {self.height}")


# Usage
r = Rectangle(5, 3)

print(r.area())       # 15
print(r.perimeter())  # 16
r.describe()          # Rectangle: 5 x 3