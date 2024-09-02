"""
Author: Oleg Shkolnik יא9.
Description: Program defines class Shape that gets color, area, perimeter and type of shape.
             Class can return color and has sentence for printing.
Date: 19/08/24
"""


class Shape:
    def __init__(self, color='black', area=3.14, perimeter=6.28, shape='circle'):
        # all values of the class
        self.color = color
        self.area = area
        self.shape = shape
        self.perimeter = perimeter

    def set_color(self, color):
        # function sets color
        self.color = color

    # functions that return all values of the class
    def get_color(self):
        return self.color

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter

    def get_shape(self):
        return self.shape

    def __str__(self):
        # if user will print class variable "shape" or its descendants will see this sentence
        return f'The {self.shape} is {self.color}; its area is {self.area} and its perimeter is {self.perimeter}'
