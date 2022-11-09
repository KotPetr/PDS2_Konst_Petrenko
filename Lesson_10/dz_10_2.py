import sys

def is_unique_collection(ls):
    try:
        if min(isinstance(x, (int, float, complex)) for x in ls):
            return len(ls) == len(set(ls))
        else:
            raise TypeError ('List contains non-numeric values.')

    except TypeError as ex:
        print(str(ex).capitalize(), file=sys.stderr)

    except Exception as ex:
        print(str(ex).capitalize(), file=sys.stderr)



print('1', is_unique_collection(range(10)))

print('2', is_unique_collection([2, 6.4, 7, 1.1, 3, 2]))

print('3', is_unique_collection('sdg'))

print('4', is_unique_collection(True))




