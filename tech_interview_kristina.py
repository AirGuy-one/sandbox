import time


def cache(func):
    results: dict[int, int] = {}

    def wrapper(n):
        try:
            return results[n]
        except KeyError:
            result_func = results[n] = func(n)
            return result_func

    return wrapper

# count = cache(count)
# cache(count)(1)
# count(1) == wrapper(1)

@cache
def count(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 2
    start = 2
    prev_, prev = 2, 3
    for i in range(start, n):
        auxiliary = prev + prev_
        prev_ = prev
        prev = auxiliary
    return prev


print(count(1))
print(count(0))
print(count(0))
print(count(1))
print(count(3))
print(count(4))

n_ = 1300

start = time.time()
print(count(n_))
end_time = time.time() - start
print('%.3g' % end_time)

start = time.time()
print(count(n_))
end_time = time.time() - start
print('%.3g' % end_time)
