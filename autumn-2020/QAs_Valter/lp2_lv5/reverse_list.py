def reverse(l):
    for i in range(len(l) // 2):
        l[i], l[-1 - i] = l[-1 - i], l[i]
