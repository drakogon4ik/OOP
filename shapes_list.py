"""
Author: Oleg Shkolnik יא9.
Description: Program defines class Container that generates list of n random shapes.
             Class can return sum of areas, sum of perimeters and
             how many shapes each color program generated as a dictionary.
Date: 2/09/24
"""


import random
from shapes import *


class Container:
    def __init__(self):
        """
        start parameters:
        shapes - list of shapes
        colors - list with colors for randomizer
        nums - list with numbers for randomizer
        """
        self.shapes = []
        self.colors = ['red', 'green', 'blue', 'black', 'white']
        self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def generate(self, n):
        # function that generates random shapes and put them into list shapes
        for i in range(n):
            rand = random.randint(1, 3)
            color = random.choice(self.colors)
            if rand == 1:
                radius = random.choice(self.nums)
                self.shapes.append(Circle(color, radius))
            elif rand == 2:
                x = random.choice(self.nums)
                y = random.choice(self.nums)
                self.shapes.append(Rectangle(color, x, y))
            else:
                x = random.choice(self.nums)
                self.shapes.append(Square(color, x))

    def sum_areas(self):
        # function makes sum of all area in list shapes
        ar_sum = 0
        for i in self.shapes:
            ar_sum += i.get_area()
        return ar_sum

    def sum_perimeters(self):
        # function makes sum of all perimeters in list shapes
        perm_sum = 0
        for i in self.shapes:
            perm_sum += i.get_perimeter()
        return perm_sum

    def count_colors(self):
        # function makes dictionary with number of each color in the list shapes
        colors_dict = {}
        for i in self.colors:
            counter = 0
            for j in self.shapes:
                if i == j.get_color():
                    counter += 1
            colors_dict[i] = counter
        return colors_dict


def main():
    # example from point 3
    my_container = Container()
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())


if __name__ == '__main__':
    new_shape = Shape('black', 4, 8, 'square')
    assert new_shape.get_color() == 'black'
    new_shape.set_color('red')
    assert not new_shape.get_color() == 'black'
    assert new_shape.get_shape() == 'square'
    assert new_shape.get_area() == 4
    assert new_shape.get_perimeter() == 8

    new_circle = Circle('red', 3)
    assert new_circle.get_area() == math.pi * 9
    assert new_circle.get_perimeter() == math.pi * 6

    new_rectangle = Rectangle()
    assert new_rectangle.get_area() == 2
    assert new_rectangle.get_perimeter() == 6

    new_square = Rectangle('black', 1, 1)
    assert new_square.get_shape() == 'square'

    true_square = Square('red', 3)
    assert true_square.get_area() == 9
    assert true_square.get_perimeter() == 12

    main()
