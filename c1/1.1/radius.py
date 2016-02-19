#! /usr/bin/env python
'''Input a radius of a sphere and get more output than you'd ever want'''
from math import pi


class radius:
    '''Creates an instance of a radius. Assigns instance variables
    for the calculations we want.
    '''
    def __init__(self, rad):
        self.radius = rad
        self.diameter = self._get_diameter()
        self.circumference = self._get_circumference()
        self.area = self._get_area()
        self.volume = self._get_volume()

    def _get_diameter(self):
        diameter = self.radius * 2
        return diameter

    def _get_circumference(self):
        circumference = self.diameter * pi
        return circumference

    def _get_area(self):
        square_rad = self.radius ** 2
        area = square_rad * 4 * pi
        return area

    def _get_volume(self):
        rad_to_third = self.radius ** 3
        volume = (4 * pi * rad_to_third) / 3
        return volume


def main():
    '''Gets input and puts results on the screen.'''
    this_rad = input("Enter Radius: ")
    try:
        rad = float(this_rad)
    except ValueError:
        print("That's not a number.")
        main()
    radius_inst = radius(rad)
    print('Diameter is %.2f' % radius_inst.diameter)
    print('Circumference is %.2f' % radius_inst.circumference)
    print('Area is %.2f' % radius_inst.area)
    print('Volume is %.2f' % radius_inst.volume)

if __name__ == '__main__':
    main()
