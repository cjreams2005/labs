from functools import lru_cache
import time

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
    
@lru_cache(maxsize=None)
def recur_fibo_memo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo_memo(n-1) + recur_fibo_memo(n-2))

n = 35
start_time = time.time()
print("Original recur_fibo(35):", recur_fibo(n))
end_time = time.time()
print("Execution time (original):", end_time - start_time, "seconds")

start_time = time.time()
print("Original recur_fibo(35):", recur_fibo(n))
end_time = time.time()
print("Execution time (original):", end_time - start_time, "seconds")