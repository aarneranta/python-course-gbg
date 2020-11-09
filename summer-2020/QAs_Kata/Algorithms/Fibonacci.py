# recursive version
def fib_rec(num):
    if num == 1 or num == 0:
        return 1
    return fib_rec(num-1) + fib_rec(num-2)


print(fib_rec(0))
print(fib_rec(1))
print(fib_rec(2))
print(fib_rec(3))
print(fib_rec(4))
print(fib_rec(5))
print(fib_rec(10))


# version using the memory
fib_series = [0 for _ in range(1000)]


def fib_mem(num):
    if num == 0 or num == 1:
        return 1
    if fib_series[num] != 0:
        return fib_series[num]
    fib_series.insert(num, (fib_mem(num-1) + fib_mem(num-2)))
    return fib_series[num]


print(fib_mem(0))
print(fib_mem(10))
print(fib_mem(2))
print(fib_mem(3))
print(fib_mem(5))
