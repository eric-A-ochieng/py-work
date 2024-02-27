# program to calculate area and perimeter of a circle

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


circle1 = Circle(radius=7)


area_result = circle1.area()
perimeter_result = circle1.perimeter()

print("Area of the circle:", area_result)
print("Perimeter of the circle:", perimeter_result)
