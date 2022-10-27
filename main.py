# 1st commit
def max_of_two(a, b):
    return a if a > b else b

print(max_of_two(8, 7))

def max_of_sequence(seq):
    max_elem = seq[0] if len(seq) > 0 else 0
    for elem in seq:
        max_elem = elem if elem > max_elem else max_elem
    return max_elem

print(max_of_sequence([7, 9 , -4]))

def print_message(string : str):
    print(string)

print_message('Hello GitHub!')

def count_negative(sequense):
    return len([x for x in sequense if x < 0])

print(count_negative((3, 8, -5, 0, -2, 2)))
