"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner

"""


class Point:
    def __init__(self, x, y, z):
        if not isinstance(x, int):
            raise TypeError
        if not isinstance(y, int):
            raise TypeError
        if not isinstance(z, int):
            raise TypeError
        self.x = x
        self.y = y
        self.z = z

    def get_distance(self, origin=None):
        if isinstance(origin, (float, int, str, list, dict, tuple)):
            raise TypeError
        elif origin:
            return ((self.x - origin.x)**2 + (self.y - origin.y)**2
                    + (self.z - origin.z)**2)**0.5
        else:
            return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __str__(self):
        return f"Point: {self.x, self.y, self.z}"
