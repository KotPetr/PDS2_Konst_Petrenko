import sys

class NegativeArgs(Exception):

    def __init__(self, *args):
        if args:
            self._args = (args)
        else:
            self._args = None

    def __str__(self):
        return f"Some of arguments {self._args} are negative."


class Parallelogram:

    def __init__(self, length : float, width = 1.0):
        if length >= 0 and width >= 0:
            self.__length = length
            self.__width = width
        else:
            raise NegativeArgs(length, width)

    def get_area(self):
        return self.__length * self.__width



try:
    a = Parallelogram(2, 5)
    print(a.get_area())
    b = Parallelogram(2, -5)
    print(b.get_area())

except NegativeArgs as ex:
    print(ex, file=sys.stderr)

except Exception as ex:
    print(ex, file=sys.stderr)

