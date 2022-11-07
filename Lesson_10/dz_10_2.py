import sys

def is_unique_collection(ls):
    try:
        return len(ls) == len(set(ls))
    except TypeError as ex:
        print(ex, file=sys.stderr)
    except Exception as ex:
        print(ex, file=sys.stderr)
    finally:
        print('_____________')



print('1', is_unique_collection(range(10)))

print('2', is_unique_collection(True))

print('3', is_unique_collection([2, 6, 7, 1, 3, 2]))





# try:
#     print(is_unique_list([2, 6, 7, 1, 3, 2]))
#     print(is_unique_list(['a', 'b', 7, False, 3.5, None]))
#     print(is_unique_list((3, 4, 1, 2)))
#
#     #print(is_unique_list('fgf', 3))
#     #print(is_unique_list(zgffdg))
#     print(is_unique_list())
#
# except TypeError as ex:
#     print(str(ex).capitalize(), file=sys.stderr)
#
# except NameError as ex:
#     print(str(ex).capitalize(), file=sys.stderr)
#
# finally:
#     print()
#     print('Program finished.')