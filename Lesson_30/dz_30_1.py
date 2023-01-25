'''
1. Написати клас для створення і роботи з хеш-таблицями. Клас повинен містити наступні функції:
- створення хеш-таблиці заданої довжини;
- пошук, додавання і видалення нових елементів;
- друкування хеш-таблиці;
- виправлення колізій;
'''

class HashTable:

    def __init__(self, size : int):
        self.size = size
        self.hash_table = [[]] * size

    def __str__(self):
        return ''.join(map(str, self.hash_table))


    def add(self, key : int, data):
        index = key % self.size
        if not self.hash_table[index]:
            self.hash_table[index] = [key, data]
        else:
            self.hash_table[index].extend([key,data])


    def search(self, key):
        index = key % self.size
        if self.hash_table[index]:
            return self.hash_table[index][self.hash_table[index].index(key) + 1]
        else:
            return None


    def remove(self, key: int, data):
        index = key % self.size
        result = self.search(key)
        if result:
            if data in self.hash_table[index]:
                self.hash_table[index].remove(key)
                self.hash_table[index].remove(data)
            else:
                error = ValueError(f'There is no \'{data}\' data with the key ({key}).')
                raise error
        else:
            error = KeyError(f'There is no key ({key}) in the hash table.')
            raise error



ht = HashTable(11)
ht.add(2, 'apple')
ht.add(8, 'pear')
ht.add(7, 'cherry')
ht.add(11, 'grape')
ht.add(22, 'pineapple')
print(ht)
print('*'* 30)

print(ht.search(3))    # None
print(ht.search(22))   # pineapple
print(ht.search(7))    # cherry
print('*'* 30)

#ht.remove(3, 'pineapple')   # KeyError
#ht.remove(22, 'pine')       # ValueError
ht.remove(22, 'pineapple')
ht.remove(8, 'pear')
print(ht)

