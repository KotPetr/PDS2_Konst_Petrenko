#1. Причина конфлікту полягає в тому, що розробка велась паралельно у 2х гілках master і test
#   тому виникли дві версії одного і того ж файлу main.py

def main_function(string : str):
    print(string)

main_function('Привіт Git!')

def max_of_sequence(seq):
    max_elem = seq[0] if len(seq) > 0 else 0
    for elem in seq:
        max_elem = elem if elem > max_elem else max_elem
    return max_elem

print(max_of_sequence([7, 9 , -4]))
print(max_of_sequence({}))

def count_negative(sequense):
    return len([x for x in sequense if x < 0])

print(count_negative((3, 8, 3, 0, -5, 2)))

def max_of_two(a, b):
    return a if a > b else b

print(max_of_two(8, 8))

tup = (2, 3, 7, 8)
print(tup)

string = 'Hello Git!'
print(string.upper())
print(string)