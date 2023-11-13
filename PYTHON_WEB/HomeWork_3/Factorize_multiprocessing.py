import multiprocessing
import time

def factorize_single(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    factors_list = []
    for number in numbers:
        factors_list.append(factorize_single(number))
    return factors_list

def factorize_parallel(*numbers):
    num_cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_cores)
    factors_list = pool.map(factorize_single, numbers)
    pool.close()
    pool.join()
    return factors_list

if __name__ == "__main__":
    numbers = (128, 255, 99999, 10651060)

    start_time = time.time()
    a, b, c, d = factorize(*numbers)
    end_time = time.time()
    print("Synchronous factorization:")
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)
    print("Time elapsed for synchronous factorization:", end_time - start_time, "seconds")

    start_time = time.time()
    a, b, c, d = factorize_parallel(*numbers)
    end_time = time.time()
    print("\nParallel factorization:")
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)
    print("Time elapsed for parallel factorization:", end_time - start_time, "seconds")