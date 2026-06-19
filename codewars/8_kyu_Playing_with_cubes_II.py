"""
https://www.codewars.com/kata/55c0ac142326fdf18d0000af

Playing with cubes II

Hey, I need help! I've got a Cube class, but it's incomplete. I need you to
implement the constructor, getter and setter methods for the side property.
The constructor should take one integer (or handle no args) and set the side
to the absolute value of the argument (if no arg, side = 0). The setter should
also use absolute value to ensure side is never negative.
"""

class Cube(object):
    def __init__(self, cube_side=0):
        self.set_side(cube_side)
    
    def get_side(self):
        return self.__side

    def set_side(self, new_side):
        self.__side = abs(new_side)
