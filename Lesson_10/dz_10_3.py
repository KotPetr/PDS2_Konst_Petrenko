import sys

# Клас помилки, яка повідомляє про негативні або нульові значення довжини або ширини
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
        # Якщо один з переданих параметрів менше або дорівнює 0 викликається помилка
        if length >= 0 and width >= 0:
            self.__length = length
            self.__width = width
        else:
            raise NegativeArgs(length, width)

    @property
    def length(self):
        return self.__length
    @property
    def width(self):
        return self.__width

    def get_area(self):
        return self.length * self.width



try:
    a = Parallelogram(2, 5)
    print(f'Площа прямокутника з длинами сторін {a.length, a.width} дорівнює {a.get_area()}')
    b = Parallelogram(2, -5)
    print(f'Площа прямокутника з длинами сторін {b.length, b.width} дорівнює {b.get_area()}')

except NegativeArgs as ex:
    print(ex, file=sys.stderr)

except Exception as ex:
    print(ex, file=sys.stderr)

