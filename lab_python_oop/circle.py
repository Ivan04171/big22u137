import math
from lab_python_oop.shape import Shape
from lab_python_oop.color import Color


class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)

    def area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return f"Circle(radius={self.radius}, color={self.color.color}, area={self.area()})"
