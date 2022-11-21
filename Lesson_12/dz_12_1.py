from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time

def compare_methods():
    def factorial(n):
        i = 1
        for x in range(1, n + 1):
            i *= x
        return i

    def thread_pool(func, num):
        res_list = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            start = time.perf_counter()
            for i in range(10):
                future = executor.submit(func, num)
                res_list.append(future.result())
        t = time.perf_counter() - start
        return t, res_list

    def process_pool(func, args):
        res_list = []
        with ProcessPoolExecutor(max_workers=10) as executor:
            start = time.perf_counter()
            for item in executor.map(factorial, args):
                res_list.append(item)
        t = time.perf_counter() - start
        return t, res_list

    t1, ls1 = thread_pool(factorial, 100)

    factorial_args = [100] * 10
    t2, ls2 = process_pool(factorial, factorial_args)

    if t1 > t2:
        print(f'Method process_pool is faster. It completes for {t2} sec.\nResult:')
        for i in ls2:
            print(i)
    else:
        print(f'Method thread_pool is faster. It completes for {t1} sec.\nResult:')
        for i in ls1:
            print(i)


compare_methods()

