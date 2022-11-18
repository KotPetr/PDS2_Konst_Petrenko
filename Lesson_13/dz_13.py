import random, time
from random_word import RandomWords

r = RandomWords()
int_list = []
float_list = []
str_list = []

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))

    # Вікторе, подивіться будь ласка, чому у мене генерація англ. слів працює дуже повільно?
    # Приблизно 0.5 сек генерується одне слово.
    str_list.append(r.get_random_word())


class SortAlgorithms:

    # Selection Sort Algorithm
    @classmethod
    def selection_sort(cls, data):
        for scanIndex in range(0, len(data)):
            minIndex = scanIndex
            for compIndex in range(scanIndex + 1, len(data)):
                if data[compIndex] < data[minIndex]:
                    minIndex = compIndex
            if minIndex != scanIndex:
                data[scanIndex], data[minIndex] = data[minIndex], data[scanIndex]


    # Insertion Sort Algorithm
    @classmethod
    def insertion_sort(cls, data):
        for scanIndex in range(1, len(data)):
            tmp = data[scanIndex]
            minIndex = scanIndex
            while minIndex > 0 and tmp < data[minIndex - 1]:
                data[minIndex] = data[minIndex - 1]
                minIndex -= 1
            data[minIndex] = tmp

    # Heap Sort Algorithm
    @classmethod
    def __heapify(cls, nums, heap_size, root_index):

        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        if left_child < heap_size and nums[left_child] > nums[largest]:
            largest = left_child

        if right_child < heap_size and nums[right_child] > nums[largest]:
            largest = right_child

        if largest != root_index:
            nums[root_index], nums[largest] = nums[largest], nums[root_index]
            cls.__heapify(nums, heap_size, largest)

    @classmethod
    def heap_sort(cls, nums):
        n = len(nums)
        for i in range(n, -1, -1):
            cls.__heapify(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            cls.__heapify(nums, i, 0)


def time_for_sort(func_for_sort, data, iter_sort):
    total_time = 0
    for i in range(iter_sort):
        start = time.perf_counter()
        func_for_sort(data)
        proc_time = time.perf_counter() - start
        total_time += proc_time
        print(f'Iteration {i+1}, process time: {proc_time} ')

    return total_time/iter_sort


if __name__ == '__main__':
    t = time_for_sort(SortAlgorithms.selection_sort, float_list, 10)
    print(f'Average time for sort: {t}')



