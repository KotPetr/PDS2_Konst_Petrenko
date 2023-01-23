'''2. Написати програми для реєстрації і авторизації користувача з наступним функціоналом:
- отримання в інтерактивному режимі логіну і пароля користувача;
- верифікація пароля і його шифрування за алгоритмом обраним алгоритмом шифрування;
- запис пари "логін-пароль" у словник з перевіркою на колізії;
- авторизація користувача за логіном і паролем.
'''
import hashlib

def write_to_file(file_name : str, dictionary):
    with open(file_name, 'w') as f:
        for k, v in dictionary.items():
           f.write(f'{k} {v}\n')
    f.close()

def registration():
    while True:
        login = input('Register please, enter your login: ')
        if login in hash_pass_table:
            print('Login alredy used. Try again.')
        else:
            while True:
                pass1 = input('Enter your password: ')
                pass2 = input('Confirm your password: ')
                if pass2 == pass1:
                    pass_hash = hashlib.md5(pass2.encode())
                    hash_pass_table[login] = pass_hash.hexdigest()
                    print('Registration completed. Access granted.')
                    write_to_file('pass.txt', hash_pass_table)
                    break
                else:
                    print('Password does not match. Please try again.')
            break

def read_from_file(file_name : str):
    my_dict = {}
    with open(file_name, mode='r', encoding='utf-8') as f:
       for line in f:
           ls = line.split()
           my_dict[ls[0]] = ls[1]

    return my_dict

def authorization():
    while True:
        login = input('Please, enter your login: ')
        if login in hash_pass_table:
            count = 0
            while True and count < 3:
                count += 1
                password = input('Enter your password: ')
                pass_hash = hashlib.md5(password.encode())
                if hash_pass_table[login] != pass_hash.hexdigest():
                    if count != 3:
                        print(f'Unknown password. Please try again. {3 - count} attempts left.')
                    else:
                        print('Incorrect password. Access denied.')
                else:
                    print('Access granted.')
                    break
            break

        else:
            print('Unknown login.')
            choice = input('Please (T)ry again or (R)egister new account or any key to exit.')
            if choice.lower() == 'r':
                registration()
                break
            elif choice.lower() == 't':
                continue
            else:
                print('Unknown input.')
            break


if __name__ == '__main__':

    hash_pass_table = read_from_file('pass.txt')

    authorization()



