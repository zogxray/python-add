from math import hypot


class Case(object):
    def __init__(self):
        self.sx = 0
        self.sy = 0
        self.aw = 0
        self.routes = []

    def add_route(self, route):
        self.routes.append(route)

    def set_sx(self, x):
        self.sx = self.sx + x / len(self.routes)

    def set_sy(self, y):
        self.sy = self.sy + y / len(self.routes)

    def set_aw(self, x, y):
        aw = hypot(self.sx - x, self.sy - y)

        if self.aw < aw:
            self.aw = aw

