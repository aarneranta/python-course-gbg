def square_root(num):
    # Räcker att kolla upp till math.sqrt(num) egentligen
    for i in range(1, num):
        if i*i == num:
            return i
    # Om vi inte har hittat en rot
    print("No integer square root!")
    return None
