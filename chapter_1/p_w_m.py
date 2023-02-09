import math
#defining a class
class Point:

    def __init__(self, x=0, y=0):
        '''Initialize the position of a new point. The x and y

        coordinates can be specified. If they are not, the

        point defaults to the origin.'''
        self.move(x, y)

    def reset(self):
        'Reset the point back to the geometric origin: 0, 0'
        self.move(0, 0)

    def move(self, x, y):
        "Move the point to a new location in 2D space."
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second point passed as a parameter.

        This function uses the Pythagorean Theorem to calculate

        the distance between the two points. The distance is

        returned as a float."""
        return math.sqrt((self.x-other_point.x)**2+(self.y-other_point.y)**2)

"""
point1 = Point()
point2 = Point()

point1.reset()
point2.move(5,0)

print(point2.calculate_distance(point1))

assert (point2.calculate_distance(point1) == point1.calculate_distance(point2))

point1.move(3,4)

print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))
"""

point = Point(3, 5)
print(point.x, point.y)

#defining a class within a function

def format_string(string, formatter=None):

    '''Format a string using the formatter object, which

    is expected to have a format() method that accepts

    a string.'''

    class DefaultFormatter:

        '''Format a string in title case.'''

        def format(self, string):

            return str(string).title()

    if not formatter:

        formatter = DefaultFormatter()

    return formatter.format(string)

hello_string = "hello world, how are you today?"

print(" input: " + hello_string)

print("output: " + format_string(hello_string))