from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time

def factorial(n):
    i = 1
    for x in range(1, n+1):
        i *= x
    return i

factorial_args = [100 * 10]
f = factorial

with ThreadPoolExecutor(max_workers=5) as executor:
    start = time.perf_counter()
    for i in range(10):
        future = executor.submit(factorial, 100)
        print(future.result())
    print(f'Time: {time.perf_counter() - start}')
print('-' * 160)


with ProcessPoolExecutor() as executor:
    started_at = time.time()
    for item in executor.map(f, factorial_args):
        print(item)
    t1 = time.time() - started_at
    result['ProcessPoolExecutor'] = t1
    print(f'Time in ProcessPoolExecutor: {t1}')





with ProcessPoolExecutor() as executor:
    fut = executor.submit(factorial, 100)
    print(fut.result())



# st = time.perf_counter()
# factorial(30)
# factorial(30)
# factorial(30)
# print(time.perf_counter() - st)