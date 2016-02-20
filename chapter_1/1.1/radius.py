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
        '''Calculate diameter of the sphere.'''
        diameter = self.radius * 2
        return diameter

    def _get_circumference(self):
        '''Calculate circumference of the sphere.'''
        circumference = self.diameter * pi
        return circumference

    def _get_area(self):
        '''Calculate area of the sphere.'''
        square_rad = self.radius ** 2
        area = square_rad * 4 * pi
        return area

    def _get_volume(self):
        '''Calculate the volume of the sphere.'''
        rad_to_third = self.radius ** 3
        volume = (4 * pi * rad_to_third) / 3
        return volume


def main():
    '''Gets input and puts results on the screen.'''
    this_rad = input("Enter Radius: ")
    try:
        f_rad = float(this_rad)
        radius_inst = radius(f_rad)
        print('Diameter is %.2f' % radius_inst.diameter)
        print('Circumference is %.2f' % radius_inst.circumference)
        print('Area is %.2f' % radius_inst.area)
        print('Volume is %.2f' % radius_inst.volume)
    except ValueError:
        print("That's not a number.")
        main()

if __name__ == '__main__':
    main()
