"""
Author: Oleg Shkolnik יא9.
Description: Program defines classes Circle, Rectangle, Square shape that get color and radius or side.
             These classes inherit from class Shape, so have the same functions.
             Program also has function compound that combine two squares or
             rectangles or square and rectangle and create new shape.
Date: 19/08/24
"""


import math
from shape import *


class Circle(Shape):

    def __init__(self, color='black', radius=1):
        # class gets radius and then inherits all functions of the class Shape
        self.radius = radius
        super().__init__(color, math.pi * pow(radius, 2), 2 * math.pi * self.radius, 'circle')


class Rectangle(Shape):

    def __init__(self, color='black', x=1, y=2):
        # class gets two sides and then inherits all functions of the class Shape
        self.x = x
        self.y = y
        super().__init__(color, x*y, (self.x + self.y) * 2, 'rectangle')

        # if user chose class rectangle, but two sides are the same, function changes his type to square
        if x == y:
            self.shape = 'square'


class Square(Rectangle):

    def __init__(self, color='black', x=1):
        # class gets side and then inherits all functions of the class Shape
        self.x = x
        super().__init__(color, self.x, self.x)
        self.shape = 'square'


def compound(shape1: Rectangle, shape2: Rectangle):
    # function that can receive only rectangle or square and creates new shape by combining them
    if not isinstance(shape1, Rectangle) or not isinstance(shape2, Rectangle):
        raise TypeError("Error, didn't receive two objects of the required type.")
    new_color = 'black'
    new_area = shape1.get_area() + shape2.get_area()
    new_perimeter = shape1.get_perimeter() + shape2.get_perimeter()
    new_shape = 'compounded_shape'
    return Shape(new_color, new_area, new_perimeter, new_shape)
