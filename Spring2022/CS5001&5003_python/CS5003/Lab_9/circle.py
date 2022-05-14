"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner

"""


class Circle:
    def __init__(self, x, y, r):
        if not isinstance(x, float):
            raise TypeError
        if not isinstance(y, float):
            raise TypeError
        if not isinstance(r, float):
            raise TypeError
        if r < 0.0:
            raise ValueError
        self.x = x
        self.y = y
        self.radius = r

    def get_area(self):
        return 3.14 * self.radius**2

    def get_distance(self, x=0.0, y=0.0):
        if not isinstance(x, float):
            raise TypeError
        if not isinstance(y, float):
            raise TypeError
        else:
            return ((self.x - x)**2 + (self.y - y)**2)**0.5

    def __str__(self):
        return f"Circle: center at {self.x, self.y} " \
               f"with radius {self.radius}"
