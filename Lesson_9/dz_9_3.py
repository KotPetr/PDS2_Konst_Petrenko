
class Parallelogram:

    def __init__(self, length : float, width = 1.0):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

    @property
    def length(self):
        return self.__length


class Square(Parallelogram):

    def get_area(self):
        return super().length **2



a = Parallelogram(3, 4)
print(a.get_area())

b = Square(3)
print(b.get_area())