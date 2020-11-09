from time import sleep, time


def move_condition(order):
    source, target = order[0], order[1]
    source_len, target_len = len(source), len(target)

    # These conditions determine if we should append to target or source
    if target_len == 0 and source_len != 0:
        target.append(source.pop())
    elif source_len == 0 and target_len != 0:
        source.append(target.pop())
    elif target[-1] > source[-1]:
        target.append(source.pop())
    else:
        source.append(target.pop())


def solve(n, A, B, C):
    order = [(A, C), (A, B), (B, C)] if n % 2 != 0 else [(A, B), (A, C), (B, C)]
    index = 0
    while C != list(range(n, 0, -1)):
        move_condition(order[index])
        print(A, B, C)
        index = index + 1 if index != 2 else 0


n = 4
A = list(range(n, 0, -1))
B = []
C = []
start_time = time()
solve(len(A), A, B, C)
end_time = time()
print("Elapsed time:", end_time - start_time)