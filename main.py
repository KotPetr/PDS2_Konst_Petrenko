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