#1. Причина конфлікту полягає в тому, що розробка велась паралельно у 2х гілках master і test,
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


# 4th commit to master
print()
print('"Test" branch was created!')

# 5th commit to test
def test_function():
    print("This function was wrote in 'Test' branch!")

# 6th commit to test
print()
print('This is "test" branch!')

