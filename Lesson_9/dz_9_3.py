
class Parallelogram:

    def __init__(self, length : float, width : float):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__width * self.__length



class Square(Parallelogram):

    def __init__(self, length: float):
        self.__length = length


    def get_area(self):
        return self.__length **2



a = Parallelogram(2, 3)
print(a.get_area())

b = Square(4)
print(b.get_area())