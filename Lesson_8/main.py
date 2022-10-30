#1. Причина конфлікту полягає в тому, що розробка велась паралельно у 2х гілках master і test
#   тому виникли дві версії одного і того ж файлу main.py


# 1st commit
def main_function():
    print('Hello Git!')

# 2nd commit
print()
print('This is "master" branch!')

# 3d commit
print()
print('This is local repository!')

def test_function():
    print("This function was wrote in 'Test' branch!")