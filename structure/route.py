from math import sin, cos, radians


class Route(object):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.commands = []

    def turn(self, radius):
        self.r = self.r+radius

    def add_command(self, command):
        self.commands.append(command)

    def change_pos(self, steps):
        rads = radians(self.r)
        self.x = self.x+steps*cos(rads)
        self.y = self.y+steps*sin(rads)

