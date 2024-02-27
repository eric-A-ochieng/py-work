# creating a class
class Circle:
    def __init__(self, radius): 
        self.radius = radius 
    def area(self):
         return 3.142 * self.radius**2
my_circle=Circle(8)
print("Radius",my_circle.radius)
print("Area",my_circle.area())
